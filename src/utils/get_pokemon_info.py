import requests
from firebase_admin import credentials, firestore, initialize_app
# credits: https://pokeapi.co/docs/v2

pkm_obj_list = []
starting_id = 1
ending_id = 10
print("Starting")
for id in range(starting_id, ending_id + 1):
    print(f"Getting: {id}... ", end="")
    response: dict = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}").json()
    extra_response: dict = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}").json()

    for name in extra_response.get("names"):
        if name["language"]["name"] == "ja-Hrkt":
            extra_response["names"] = name["name"]
            break
    types = []
    for type in response.get("types"):
        types.append(type["type"]["name"])

    pkm_obj = {
        "id": id,
        "name": response.get("name"),
        "name_jp": extra_response.get("names"),
        "sprites": response["sprites"]["other"]["home"].get("front_default"),
        "types": types,
        "evolves_from": extra_response.get("evolves_from_species")
    }
    pkm_obj_list.append(pkm_obj)
    print("  DONE!")



# Initialize Firebase Admin SDK with your credentials file
cred = credentials.Certificate('src/utils/firebase_credentials.json')
initialize_app(cred)

db = firestore.client()
batch = db.batch()

# gets collection called "pokemons"
collection_ref = db.collection('pokemons')

for pkm in pkm_obj_list:
    num = str(pkm['id'])
    id = num.zfill(3)
    doc_ref = collection_ref.document(id)  # Manually set document ID
    batch.set(doc_ref, pkm)
batch.commit()
