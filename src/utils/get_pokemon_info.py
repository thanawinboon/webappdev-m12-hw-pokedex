import requests
import json 
# credits: https://pokeapi.co/docs/v2

pkm_obj_list = []
starting_id = 1
ending_id = 151
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
    print(" DONE!")

pkm_list = {"pokemons": pkm_obj_list}

with open("./pokedex.json", "w", encoding='utf8') as file:
    result = json.dumps(pkm_list, indent=4, ensure_ascii=False)
    file.write(result)
