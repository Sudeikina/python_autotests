import requests

token = "fe56a1625745ecc5f59d11fa9e03f9d3"

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Polina",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type": "application/json", "trainer_token": token})

print(response.text)

if response.status_code == 201:
    print('ok!')
else:
    print('not ok!')

change_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "12265",
    "name": "New Name"
}, headers = {"Content-Type": "application/json", "trainer_token": token})

print(change_name.text)

if change_name.status_code == 200:
    print('ok!')
else:
    print('not ok!')

add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "12268"
}, headers = {"Content-Type": "application/json", "trainer_token": token})

print(add_pokeball.text)

if add_pokeball.status_code == 200:
    print('ok!')
else:
    print('not ok!')