import requests
from time import sleep
from random import randint
from moves import Move_tutor
# from moves import runMoves

def start():        
        while True:
            user = input("What is your name? ")
            print(f"{user.title()}, you will be given a team of 6 random pokemon to train.")
            sleep(1)
            # Give the user a party of pokemon to start with
            # Random number generated for each pokemon id
            random_team = [randint(1,898) for i in range(6)]
            # print(random_team) # This shows the numbers, I want just the names
            def poke_api_call_by_id(pokemon):
                req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
                if req.status_code == 200:
                    data = req.json()
                
                    name = data['name']
                    types = [pokemon['type']['name'] for pokemon in data['types']]
                    abilities = [pokemon['ability']['name'] for pokemon in data['abilities']]
                    weight = data['weight']
                
                    poke = {
                        "name": name,
                        'abilities': abilities,
                        'weight': weight,
                        'types' : types
                    }
                    return poke
            my_six_pokemon = {}
            for id in random_team:
                poke_stats = poke_api_call_by_id(id)
                my_six_pokemon[poke_stats['name'].title()] = poke_stats
            for key, value in my_six_pokemon.items():
                print(key)

            global selected
            selected = input("Which of your pokemon do you want to select? ")
            if selected.title() in my_six_pokemon:
                # Options to do stuff with pokemon after getting them
                response = input("What would you like to do? (evolve, train, quit) ")
                if response.lower() == "evolve":
                    print("EVOLVING")
                    # Move_tutor.runMoves()
                elif response.lower() == "train":
                    # x = input("Who would you like to train? ")
                    selected.runMoves()
                    # runMoves()
                elif response.lower == "quit":
                    print(f"Thanks for training. Go outside! Or not, I'm not your mom. I'm a computer. bzzzzzz")
                    break
                else:
                    print("Invalid input, please try again!")
            else:
                print("Invalid input, please try again!")



# class Catch:
    # Step one is to lay out a few random pokemon for the trainer to catch and add to their team
    
    # def poke_api_call_by_id(pokemon): # This is getting the pokemon by id
    #     req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    #     if req.status_code == 200:
    #         data = req.json()
        
    #         name = data['name']
    #         types = [pokemon['type']['name'] for pokemon in data['types']]
    #         abilities = [pokemon['ability']['name'] for pokemon in data['abilities']]
    #         weight = data['weight']
        
    #         poke = {
    #             "name": name,
    #             'abilities': abilities,
    #             'weight': weight,
    #             'types' : types
    #         }
    #         return poke
    
    # def encounter():
    # tallGrass = [randint(1,898) for i in range(6)]
    # sixRandom = {}
    # for id in tallGrass:
    #     poke_stats = poke_api_call_by_id(id)
    #     sixRandom[poke_stats['name'].title()] = poke_stats

    # print(sixRandom)

    # Step two is to make catching a 50% chance to fail
    # def catch(self):
    #     # API call for pokemon's species
    #     r = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.name}/")
    #     if r.status_code == 200:
    #         pokemon_species = r.json()
    #     else:
    #         print(f'Ran into an issue {r.status_code}')
    #         return

start()