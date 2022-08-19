import requests
from time import sleep
import evolve
import moves
import catch

class Pokemon(moves.Move_tutor, evolve.Evolver, catch.Catch):
    def __init__(self,name):
        super().__init__()
        # Move_tutor.__init__(self)
        self.name = name
        self.types = []
        self.abilities = []
        self.weight = None
        self.image = None
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f'Ran into an issue {r.status_code}')
            return
        self.name = pokemon['name']
        self.types = [pokemon['type']['name'] for pokemon in pokemon['types']]
        self.abilities = [poke['ability']['name'] for poke in pokemon['abilities']]
        self.weight = pokemon['weight']
        # new image details 
        self.image = pokemon["sprites"]["front_default"]
        print(f'\nYou\'ve got a new {self.name}!\n')
    def __repr__(self):
        return f"You caught a {self.name}!!"






# user = input("What is your name? ")
# marowak = Pokemon("marowak-alola")
# marowak.runMoves()
# start(user)