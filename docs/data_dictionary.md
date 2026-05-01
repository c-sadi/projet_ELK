# Dictionnaire de données

# Index : movies_raw
Contient les données brutes directement depuis le fichier movies.csv sans transformation.

# Index : movies_clean
Contient les données nettoyées, typées et normalisées prêtes pour l'analyse.

# Description des champs

| Champ | Type (raw) | Type (clean) | Description |
| id | text | integer | Identifiant unique du film |
| title | text | text (analyzed) | Titre du film |
| genres | text | keyword | Genre(s) du film |
| original_language | text | keyword | Langue originale du film (code ISO) |
| overview | text | text (analyzed) | Synopsis du film |
| popularity | text | float | Score de popularité TMDB |
| production_companies | text | keyword | Sociétés de production |
| release_date | text | date | Date de sortie du film |
| budget | text | long | Budget du film en dollars |
| revenue | text | long | Recettes du film en dollars |
| runtime | text | integer | Durée du film en minutes |
| status | text | keyword | Statut du film (Released, In Production...) |
| tagline | text | text | Slogan du film |
| vote_average | text | float | Note moyenne des utilisateurs sur 10 |
| vote_count | text | integer | Nombre de votes |
| credits | text | keyword | Acteurs et équipe technique |
| keywords | text | keyword | Mots-clés associés au film |
| poster_path | text | keyword | Chemin vers l'affiche du film |
| backdrop_path | text | keyword | Chemin vers l'image de fond |
| recommendations | text | keyword | Films recommandés associés |

# Analyzer personnalisé : movies_analyzer

Un analyzer personnalisé a été défini dans les paramètres de l'index movies_clean.
Il applique les traitements suivants dans l'ordre :
1. Tokenizer standard : découpe le texte en petits mots
2. Filtre lowercase : convertit tous les caractères en minuscules
3. Filtre stop : supprime les mots vides 
4. Filtre snowball : réduit les mots à leur racine 

Cet analyzer est applique sur les champs title et overview pour permettre
une recherche full-text efficace et insensible à la casse.