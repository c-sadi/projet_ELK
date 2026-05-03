# Runbook technique

Ce document décrit les étapes necessaires pour démarrer, arrêter et vérifier la plateforme Movies ELK sur une machine vierge.

# 1. Prerequis

- Docker Desktop installé et démarré
- Docker Compose disponible
- Avoir créé préalablement un repo github

# 2. Installation

# 2.1 Cloner le depot
git clone https://github.com/c-sadi/projet_ELK.git

# 2.2 Placer le dataset
Télécharger movies.csv depuis Kaggle et le placer dans le dossier 'projet_ELK\DATA\movies.csv'

# 2.3 Démarrer la stack
docker-compose up -d

# 3. Vérification des services
# 3.1 Elasticsearch
Ouvrir dans le navigateur : http://localhost:9200
Resultat attendu : JSON avec "You Know, for Search"

# 3.2 Kibana
Ouvrir dans le navigateur : http://localhost:5601
Resultat attendu : interface Kibana accessible

# 3.3 Jupyter
Ouvrir dans le navigateur : http://localhost:8888
Token : elasticlab

# 3.4 Verifier les index
Dans Kibana Dev Tools :
GET /_cat/indices?v
Les index movies_raw et movies_clean doivent être présents.

# 3.5 Vérifier le nombre de documents
GET /movies_clean/_count
GET /movies_raw/_count
Résultat attendu : environ 662 000 documents dans movies_clean.

# 4. Création du mapping movies_clean
Si l'index movies_clean n'existe pas, le créer via Kibana Dev Tools :
PUT /movies_clean
{
"settings": {
"analysis": {
"analyzer": {
"movies_analyzer": {
"type": "custom",
"tokenizer": "standard",
"filter": ["lowercase", "stop", "snowball"]
}
}
}
},
"mappings": {
"properties": {
"id":                   { "type": "integer" },
"title":                { "type": "text", "analyzer": "movies_analyzer" },
"genres":               { "type": "keyword" },
"original_language":    { "type": "keyword" },
"overview":             { "type": "text", "analyzer": "movies_analyzer" },
"popularity":           { "type": "float" },
"release_date":         { "type": "date" },
"budget":               { "type": "long" },
"revenue":              { "type": "long" },
"runtime":              { "type": "integer" },
"status":               { "type": "keyword" },
"tagline":              { "type": "text" },
"vote_average":         { "type": "float" },
"vote_count":           { "type": "integer" },
"keywords":             { "type": "keyword" },
"production_companies": { "type": "keyword" }
}
}
}

# 5. Ingestion des données
Démarrer Logstash pour ingérer les données : docker start logstash
Attendre 20 a 30 minutes que l'ingestion soit complète.
Vérifier avec : GET /movies_clean/_count.

# 6. Arrêter la stack
docker-compose down

# 7. Redémarrer proprement
docker-compose down
docker-compose up -d

# 8. Moteur de recherche

Lancer l'application Streamlit :
pip install streamlit requests
streamlit run app.py
Ouvrir dans le navigateur : http://localhost:8501