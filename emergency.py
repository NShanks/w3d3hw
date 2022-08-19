import requests
from time import sleep

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

class Move_tutor():
    def __init__(self):# init only houses attributes
        self.move_list = []
        self.availableMoves = []
        # self.getMoves()
        # self.name = Pokemon("charmander").name
    def getMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
        else:
            print(f'Ran into an issue {r3.status_code}')
            return
    def teachMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
            print("You can teach the following moves:")
            print(self.move_list)
            newOne = input("\nWhat would you like to teach it? ")
        else:
            print(f'Ran into an issue {r3.status_code}')
            return
        if len(self.availableMoves) < 4:
            if newOne in self.move_list:
                print(f"TEACHING {newOne}")
                self.availableMoves.append(newOne)
            else:
                print(f"Do you see {newOne} in that move list? NO! You think you have a mew on your hands?")
            print(f"Your {self.name} knows {self.availableMoves}")
        else:
            print("They can only know 4 at a time. Please choose a move to remove: ")
            print(self.availableMoves)
            deleteMove = input()            
            print("You can teach the following moves:")
            print(self.move_list)
            newOne = input("\nWhat would you like to teach it? ")
            if deleteMove in self.availableMoves:
                print(f"Deleting {deleteMove}")
                self.availableMoves.remove(deleteMove)
                print(f"TEACHING {newOne}")
                self.availableMoves.append(newOne)
            else:
                print(f"They do not know {deleteMove}. Please pick a move they know.")
            print(f"Your {self.name} knows {self.availableMoves}")
    
    def viewMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
            print(self.availableMoves)
            return
        else:
            print(f'Ran into an issue {r3.status_code}')
            return

    def run(self):        
        while True:
            response = input("What would you like to do? (teach, view, quit) ")
            if response.lower() == "teach":
                self.teachMoves()
            elif response.lower() == "view":
                self.viewMoves()
            elif response.lower() == "add":
                self.add_user()
            elif response.lower == "quit":
                print(f"Thanks for training. Go outside! Or not, I'm not your mom. I'm a computer. bzzzzzz")
                break
            else:
                print("Invalid input, please try again!")

class Pokemon(Move_tutor, Evolver):
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

marowak = Pokemon("marowak-alola")
# marowak.getMoves()
# print(marowak.move_list)
marowak.run()

