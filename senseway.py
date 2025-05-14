# SenseWay MVP - v0.1.1
# User pastes a block of code. We extract relevant keywords and search Stack Overflow.

import requests
import streamlit as st
import re
import urllib.parse

st.set_page_config(page_title="SenseWay MVP", layout="centered")
st.title("SenseWay - Search Real-World Errors by Code")
st.caption("Paste your code with an error. We'll search Stack Overflow for similar cases.")

code_input = st.text_area("Paste your code block here:", height=300)

def extract_keywords_from_code(code):
    error_keywords = re.findall(r"(\b[A-Z][a-z]+Error\b)", code)
    structures = ["for", "if", "while", "dict", "list", "class", "def", "return", "import", "try", "except"]
    found_structures = [s for s in structures if s in code]
    return list(set(error_keywords + found_structures))

def search_stackoverflow(keywords):
    if not keywords:
        return []
    query = "+".join(keywords)
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={encoded_query}&site=stackoverflow"
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        data = response.json()
        for item in data.get("items", [])[:5]:
            results.append({
                "title": item["title"],
                "link": item["link"],
                "is_answered": item["is_answered"]
            })
    return results

if st.button("Search for Similar Cases"):
    if code_input:
        with st.spinner("Analyzing code and searching..."):
            keywords = extract_keywords_from_code(code_input)
            results = search_stackoverflow(keywords)
            if results:
                st.success("Similar cases found:")
                for res in results:
                    st.markdown(f"### {res['title']}")
                    st.markdown(f"[View on Stack Overflow]({res['link']}) {'✅ Answered' if res['is_answered'] else '❌ Unanswered'}")
                    st.markdown("---")
            else:
                st.warning("No similar cases found. Try adjusting your code.")
    else:
        st.warning("Please paste a code block first.")
