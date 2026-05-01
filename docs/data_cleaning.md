# Documentation du nettoyage des donnees

# 1. Contexte

Le dataset movies.csv contient environ 770 000 films issus de kaggle.
Avant toute analyse, un nettoyage et une normalisation des données ont été réalisés
via le pipeline logstash.

# 2. Anomalies détectées

# 2.1 Dates aberrantes
Certains films possedent des dates de sortie incorrectes, situees dans le futur (exemple : 2090, 2099). Ces valeurs sont probablement dues à des erreurs de saisie dans la
base de données source. 
Impact : la visualisation de l'evolution par annee affichait des valeurs nulles pour les dernières années.
Solution appliquée : filtre sur les dates comprises entre 1900 et 2026.

# 2.2 Valeurs manquantes
Plusieurs champs contiennent des valeurs vides ou nulles :
- budget : 0 pour les films dont le budget n'est pas renseigné
- revenue : 0 pour les films dont les recettes ne sont pas renseignées
- overview : champ vide pour certains films
- runtime : 0 ou vide pour certains films

# 2.3 Types incorrects
Dans le fichier CSV brut, tous les champs sont lus comme du texte.
Les champs numériques et les dates doivent être convertis explicitement.

# 2.4 Doublons
Lors des tests d'ingestion, des doublons ont été détectés dans movies_raw à cause de plusieurs relances de logstash. Ce problème a été résolu en ajoutant document_id => "%{id}" dans la configuration logstash.

# 3. Règles de nettoyage appliquées dans logstash

# 3.1 Suppression de la ligne header
if [id] == "id" { drop {} } La première ligne du CSV contient les noms de colonnes. 

# 3.2 Suppression des films sans titre
if ![title] or [title] == "" { drop {} } Un film sans titre ne peut pas être exploité dans les analyses. D'allieurs on en a que 662 083 films.

# 3.3 Conversion des types numeriques
mutate {
convert => {
"popularity"   => "float"
"budget"       => "integer"
"revenue"      => "integer"
"runtime"      => "integer"
"vote_average" => "float"
"vote_count"   => "integer"
}
}

# 3.4 Parsing de la date
date {
match => ["release_date", "yyyy-MM-dd"]
target => "release_date"
}

# 3.5 Suppression des champs techniques inutiles
mutate {
remove_field => ["message", "host", "log", "@version", "event"]
}

# 3.6 Prévention des doublons
document_id => "%{id}" Utilisation de l'identifiant unique du film comme document_id Elasticsearch pour eviter les doublons en cas de reingestion.

# 4. Mesure d'impact avant/après nettoyage

| Indicateur | movies_raw | movies_clean |
| Nombre de documents | ~770 000 | ~662 000 |
| Champs types correctement | Non | Oui |
| Doublons | Possibles | Impossible (document_id) |
| Dates aberrantes | Présentes | Filtrées à la requête |
| Films sans titre | Présents | Supprimés |
| Champs techniques | Présents | Supprimés |

# 5. Conclusion

Le passage de movies_raw à movies_clean a permis de réduire le nombre de documents
d'environ 108 000 enregistrements invalides ou en doublon. Les données restantes
sont correctement typées et exploitables pour les analyses Kibana et les requêtes
Elasticsearch.