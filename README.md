# projet_ELK
Projet réalisé dans le cadre du cours sur la stack ELK. L'objectif est de construire une plateforme complète d'analyse de données cinématographiques à partir d'un dataset de 770 000 films issu de Kaggle (TMDB Movies Dataset).

# Stack technique
Tout tourne en local via Docker Compose avec 5 services : Elasticsearch (stockage et recherche), Logstash (ingestion et nettoyage), Kibana (visualisation), PostgreSQL et Jupyter (analyses).

# Pipeline de donnees
Le fichier movies.csv est ingeré via Logstash qui parse, nettoie et convertit les types avant d'indexer les données dans deux index : movies_raw (données brutes) et movies_clean (données nettoyées avec mapping explicite et analyzer personnalisé).

# Ce que le projet contient
- 12 requêtes Elasticsearch commentées dont 5 requêtes bool
- Un dashboard Kibana avec 7 visualisations métier (répartition par langue, évolution par année, top films, distribution des notes...)
- Un moteur de recherche connecté à Elasticsearch via Streamlit
- Une documentation complète dans le dossier docs/

# Gestion de projet
Gitflow respecte avec branches main, dev et feature/*. Pull Requests obligatoires pour chaque merge. Planning poker documente dans docs/planning_poker.md.
Projet réalisé individuellement.
