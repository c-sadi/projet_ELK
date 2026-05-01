import streamlit as st
import requests
import json

# =========================
# CONFIG ELASTICSEARCH
# =========================
ES_URL = "http://localhost:9200"
INDEX = "movies_clean"

# =========================
# SEARCH FUNCTION (HTTP DIRECT)
# =========================
def search_movies(query, genre=None, language=None, year_from=None):

    url = f"{ES_URL}/{INDEX}/_search"

    must = [{
        "multi_match": {
            "query": query,
            "fields": ["title^3", "overview", "tagline"]
        }
    }]

    filters = []

    if genre:
        filters.append({"term": {"genres": genre}})

    if language:
        filters.append({"term": {"original_language": language}})

    if year_from:
        filters.append({
            "range": {
                "release_date": {"gte": f"{year_from}-01-01"}
            }
        })

    body = {
        "size": 10,
        "query": {
            "bool": {
                "must": must,
                "filter": filters
            }
        },
        "sort": [
            {"popularity": "desc"}
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, data=json.dumps(body))

    return response.json()

# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Movie Search Engine", layout="wide")

st.title("🎬 Movie Search Engine (HTTP + Elasticsearch)")

query = st.text_input("🔎 Search movies")

col1, col2, col3 = st.columns(3)

with col1:
    genre = st.selectbox("🎭 Genre", ["", "Action", "Drama", "Comedy", "Horror", "Science Fiction"])

with col2:
    language = st.selectbox("🌍 Language", ["", "en", "fr", "es"])

with col3:
    year_from = st.text_input("📅 Year from")

# =========================
# SEARCH BUTTON
# =========================
if st.button("Search 🔍"):

    if not query:
        st.warning("Enter a search query")
    else:
        try:
            results = search_movies(query, genre, language, year_from)

            hits = results["hits"]["hits"]

            if len(hits) == 0:
                st.error("No movies found 😢")
            else:
                st.success(f"{len(hits)} results")

                for hit in hits:
                    movie = hit["_source"]

                    st.markdown("### 🎬 " + str(movie.get("title", "")))

                    colA, colB = st.columns(2)

                    with colA:
                        st.write("🎭 Genre:", movie.get("genres"))
                        st.write("🌍 Language:", movie.get("original_language"))
                        st.write("📅 Release:", movie.get("release_date"))

                    with colB:
                        st.write("⭐ Rating:", movie.get("vote_average"))
                        st.write("🔥 Popularity:", movie.get("popularity"))

                    st.write("---")

        except Exception as e:
            st.error("Error while searching")
            st.write(e)