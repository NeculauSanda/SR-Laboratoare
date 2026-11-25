
import json
import re
import numpy as np
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("tesco_sample.json", "r", encoding="utf-8") as f:
    produse = json.load(f)

def clean_text_html(text):
    if not text:
        return ""
    soup_text = BeautifulSoup(text, "html.parser").get_text(separator=" ")
    text_curat = re.sub(r"[^a-zA-Z0-9\s]", " ", soup_text)
    text_curat = re.sub(r"\s+", " ", text_curat).strip().lower()
    return text_curat

documente = []
for prod in produse:
    nume = prod.get("name", "")
    descriere = clean_text_html(prod.get("description", ""))
    documente.append(f"{nume} {descriere}")

vector = TfidfVectorizer(stop_words="english")
matrice_tfidf = vector.fit_transform(documente)

matrice_similaritate = cosine_similarity(matrice_tfidf)

print("\nMatricea de similaritate primele 5 elemente\n")
print(np.round(matrice_similaritate[:5, :5], 3))


perechi = []
for i in range(len(produse)):
    for j in range(i + 1, len(produse)): # nu luam diagonala principala si evitam dublarea perechilor
        if produse[i].get("sku") != produse[j].get("sku") and produse[i].get("name") != produse[j].get("name"):
            perechi.append((matrice_similaritate[i, j], i, j))

perechi.sort(reverse=True)

scor_max, idx1, idx2 = perechi[0]

print(f"\nCea mai similara pereche (scor: {scor_max:.4f}):")
print(f"Produs 1 [idx = {idx1}]: {produse[idx1]['name']} - SKU: {produse[idx1]['sku']}")
print(f"Produs 2 [idx = {idx2}]: {produse[idx2]['name']} - SKU: {produse[idx2]['sku']}")

print("\nTop 5 perechi asemanatoare:")
for score, i, j in perechi[:5]:
    print(f"Scor {score:.4f}: \"{produse[i]['name']}\" vs \"{produse[j]['name']}\"")

