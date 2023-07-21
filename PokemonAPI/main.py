import requests

pokemon_id = input("enter your pokemon id: ")

url = f"https://pokeapi.co/api/v2/berry/{pokemon_id}/"
response = requests.get(url)
print(response.json())