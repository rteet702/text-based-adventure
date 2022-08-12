from generic_classes.generic_statted import GenericStatted
import os

class Game:
    def __init__(self):
        self.player_character = None

    def __repr__(self):
        pass

    def start_game(self):
        Game.cls()
        print('##'*40)
        print('Welcome to the Text Based Adventure!')
        print('##'*40)

        # if the player doesn't want to play, don't play. 
        if Game.query_player('Are you ready to begin your Adventure? y/n', False).lower() == 'n':
            return 'Game Exiting...'
        
        self.create_character()

    def create_character(self) -> None:
        name_input = Game.query_player('What is your name, adventurer?')
        if name_input != '':
            self.player_character = GenericStatted(name_input)

        print(f'\nWell met, {self.player_character.name}')

    @staticmethod
    def query_player(question:str, clr:bool = True) -> str:
        if clr:
            Game.cls()
        answer = input(f'\n{question}\n\n')
        return answer

    @staticmethod
    def cls() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')