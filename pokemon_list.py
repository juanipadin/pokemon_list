import requests
import csv

def Search(data):
    url = f'https://pokeapi.co/api/v2/pokemon/{data}'
    data = requests.get(url).json()
    dict={"Name":data['forms'][0]['name'],
          "ID":data['id'],
          "Weight":data['weight'],
          "Height":data['height'],
          "Base Experience":data['base_experience']}
    with open('pokemons_details.csv', 'a',newline='') as f:
        w = csv.DictWriter(f, dict)
        w.writerow(dict)

for x in range(1,1119):
    Search(x)


