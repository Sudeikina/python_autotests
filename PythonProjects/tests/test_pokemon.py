import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'


def test_trainer_name():
    response = requests.get(f'{host}/trainers', params = {"trainer_id": 2542})
    data = response.json()
    assert data["trainer_name"] == "Nawsikaya"
