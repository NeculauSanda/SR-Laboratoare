Laborator 5

- Am eliminat tagurile html
- am normalizat textul, am eliminat caracterele non-alfabetice, spatiile multiple si conversie la literele mici
- am combinat numele produsului si descrierea curatata si am facut reprezentarea vectoriala
- am eliminat stop_words din engleza
- am facut similaritatea dintre produse folosind functia cosine_similarity si am filtrat duplicatele (produsele cu acelasi SKU sau nume identic)

-- 2 PRODUSE SIMILARE --

Cea mai similara pereche (scor: 1.0000):
Produs 1 [idx = 68]: Tesco Numerical Candle 5 - SKU: 250126336
Produs 2 [idx = 72]: Tesco Numerical Candle 6 - SKU: 250126359

Au scor de similititudine maxim deoarece fac parte din aceeasi gama de lumanari, insa difera forma lor caracter ce e ignorat cu ajutorul TF-IDF.
Ele au aceleasi specificatii, instructiuni