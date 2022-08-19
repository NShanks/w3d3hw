import requests
from time import sleep
# import moves

class Evolver: 
    def evolve(self):
        # API call for pokemon's species
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.name}/")
        if r.status_code == 200:
            pokemon_species = r.json()
        else:
            print(f'Ran into an issue {r.status_code}')
            return
        #API call for species evolutionary chain
        r2 = requests.get(pokemon_species['evolution_chain']['url'])
        if r2.status_code == 200:
            ev_chain = r2.json()
            ev_chain = ev_chain['chain']
        else:
            print(f"Ran into an issue {r2.status_code}")
            return
        base_name = ev_chain["species"]["name"]
        #print(base_name, 'base name')
        evolution = ev_chain['evolves_to'][0]
        evolution_name = evolution['species']['name']
        # Evolution 1
        if base_name == self.name:
            pass
        # Evolution 2
        elif evolution_name == self.name:
            evolution_name = evolution['evolves_to'][0]['species']['name']
        # Evolution 3
        else:
            print(f"You can't evolve your {self.name} anymore. ")
            return
        print('.......')
        sleep(1)
        print(f"Your {self.name} is evolving!?!?")
        self.display()
        sleep(1)
        print('................')
        self.name = evolution_name
        self.poke_api_call()
        self.display()