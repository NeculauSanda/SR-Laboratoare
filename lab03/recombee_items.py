import os
import pandas as pd
from dotenv import load_dotenv
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

# TODO 1: Configurare credentiale Recombee (la fel ca la Lab 02)
load_dotenv("../lab02/.env")
DB_NAME = 'lab-egv-sr-dev'
PRIVATE_TOKEN = os.getenv('RECOMBEE_PRIVATE_TOKEN')
REGION = Region.EU_WEST

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=REGION)

# TODO 2: Incarcarea aceluiasi dataset folosit la Lab 02
PATH_DATASET = '../lab02/Amazon_BestSelling_Books_500.csv'  # Schimbati cu calea catre dataset-ul vostru

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # TODO 3: Extrageti ID-ul unic al produsului din coloana corespunzatoare din CSV
        item_id = str(row['ISBN'])
        
        # TODO 4: Mapati proprietatile definite anterior cu valorile din randul curent
        # Exemplu:
        properties = {
            "title": str(row['Title']),
            "author": str(row['Author']),
            "category": str(row['Category']),
            "sub_genre": str(row['Sub-Genre']),
            "price_USD": float(row['Price (USD)']),
            "rating": float(row['Rating']),
            "reviews_count": int(row['Reviews']),
            "year_published": int(row['Year Published'])
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        # (SetItemValues creează automat item-ul dacă acesta nu există)
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    # Trimitem si restul ramanase (daca numarul total nu e multiplu de 100)
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
