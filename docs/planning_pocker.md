# Planning Poker

# 1. Participants
- Membre 1 : Lead technique (développement principal)
- Membre 2 : Responsable de données
- Membre 3 : Responsable visualisation
- Membre 4 : Responsable documentation

Note : ce projet a été réalise individuellement. Les estimations ci-dessous
ont été produites de manière retrospective pour documenter la complexité
de chaque feature.

# 2. Echelle utilisée
Suite de Fibonacci : 1, 2, 3, 5, 8, 13

# 3. Stories estimées

 User Story | Votes initiaux | Estimation finale | Hypotheses | Owner |
|Mettre en place la stack Docker avec Elasticsearch, Kibana et Logstash | 2, 3, 3, 5 | 3 | Docker Desktop installé, ports disponibles | Membre 1 |
|Ingérer les données brutes de movies.csv dans movies_raw | 3, 3, 5, 5 | 5 | Le fichier CSV est bien formé | Membre 2 |
| Nettoyer et indexer les données dans movies_clean avec mapping explicite | 5, 5, 8, 8 | 8 | Les types de champs sont identifiés | Membre 2 |
|Produire 12 requêtes Elasticsearch commentées dont 5 bool | 3, 5, 5, 5 | 5 | Les données sont correctement indexées | Membre 1 |
| Créer un dashboard Kibana avec 6 a 8 visualisations pertinentes | 5, 5, 8, 8 | 8 | Le data view movies_clean est configuré | Membre 3 |
| Implémenter un moteur de recherche connecté à Elasticsearch | 5, 8, 8, 13 | 8 | Streamlit est installé | Membre 1 |
| Produire la documentation complète du projet | 3, 3, 5, 5 | 5 | Toutes les features sont terminées | Membre 4 |

# 4. Decisions de decoupage
- Nettoyer et indexer les données dans movies_clean avec mapping explicite :
  - Découpé en deux parties : création du mapping puis ingestion nettoyée
  - Risque : format CSV instable, valeurs manquantes
  - Action : tester sur un échantillon avant l'ingestion complète

- Implémenter un moteur de recherche connecté à Elasticsearch :
  - Découpé en deux parties : backend de recherche puis interface utilisateur
  - Risque : widgets Jupyter non compatibles avec JupyterLab
  - Action : utiliser Streamlit comme alternative

# 5. Répartition finale des features

- Membre 1 : Bootstrap stack, requêtes Elasticsearch, moteur de recherche
- Membre 2 : Ingestion brute, nettoyage, mapping
- Membre 3 : Dashboard Kibana, visualisations
- Membre 4 : Documentation, runbook, dictionnaire de données