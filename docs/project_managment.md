# Gestion de projet

# 1. Organisation de l'équipe

Ce projet a été réalisé individuellement en raison de contraintes organisationnelles.
L'ensemble des features ont été développées par un seul membre.
Le Gitflow et les Pull Requests ont été respectés malgré la configuration individuelle.

# 2. Gitflow appliqué
# Branches utilisées
- main : version stable finale
- dev : branche d'integration
- feature/bootstrap-stack : mise en place de la stack Docker
- feature/ingestion-raw : ingestion brute dans movies_raw
- feature/cleaning-mapping : nettoyage et mapping movies_clean
- feature/queries : 12 requêtes Elasticsearch commentées
- feature/dashboard : visualisations Kibana
- feature/search-engine : moteur de recherche Streamlit
- feature/documentation : fichiers de documentation

# Règles respectées
- Aucun push direct sur main ou dev
- Chaque feature developpée sur une branche séparée
- Pull Request obligatoire pour merger dans dev
- Merge de dev dans main en fin de projet

# 3. Ordre de réalisation des features
1. Bootstrap stack Docker Compose
2. Ingestion brute movies_raw
3. Nettoyage et mapping movies_clean
4. 12 requêtes Elasticsearch
5. Dashboard Kibana
6. Moteur de recherche Streamlit
7. Documentation complète

# 4. Difficultés rencontrées
- Doublons lors de la reingestion Logstash : résolu avec document_id
- Dates aberrantes dans le dataset : filtrées dans les requêtes
- Widgets Jupyter non fonctionnels : remplace par Streamlit en python
- Timeout Elasticsearch lors de la première ingestion : résolu en redémarrant les services malgré la longue durée du redémarrage

# 5. Outils utilisés
- Docker Desktop pour la containerisation
- VS Code pour l'édition des fichiers
- Kibana Dev Tools pour tester les requêtes et réaliser le dashboard
- Jupyter pour les notebooks d'analyse
- Streamlit pour le moteur de recherche
- GitHub pour le versioning