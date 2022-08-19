import requests
from time import sleep
# import evolve
# import pokemon

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

    def runMoves(self):        
        while True:
            response = input("What would you like to do? (teach, view, quit) ")
            if response.lower() == "teach":
                self.teachMoves()
            elif response.lower() == "view":
                self.viewMoves()
            elif response.lower == "quit":
                print(f"Thanks for training. Go fight!")
                break
            else:
                print("Invalid input, please try again!")