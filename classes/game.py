from generic_classes.generic_statted import GenericStatted
from random import randint
import os

class Game:
    difficulties = ['absolute beginner', 'novice', 'experienced', 'master', 'why' ]
    def __init__(self) -> None:
        self.player_character = None
        self.difficulty = ''
        self.diff_scale = 0

    def __repr__(self) -> str:
        return 'Game Object'

    def start_game(self):
        Game.cls()
        print('##'*40)
        print('Welcome to the Text Based Adventure!')
        print('##'*40)

        # if the player doesn't want to play, don't play. 
        if Game.query_player('Are you ready to begin your Adventure? y/n', False).lower() == 'n':
            return 'Game Exiting...'
        
        # Create the character! :D
        self.create_character()

        # Difficulty Settings
        self.set_difficulty()

    def create_character(self) -> None:
        # This method is called at the beginning of the game in order to create the player's main character.
        # Should this not be called... the game just is not going to work.
        name_input = Game.query_player('What is your name, adventurer?')
        if name_input != '':
            self.player_character = GenericStatted(name_input)

        print(f'\nWell met, {self.player_character.name}. Just to inform you, your stats are...')
        print('##'*40)
        for key, value in self.player_character.stats.items():
            print(f'{key.capitalize()} : {value}')
        print('##'*40)

    def set_difficulty(self) -> None:
        # This method is also called at the beginning of the game in order to set the difficulty of the player's adventure.        
        answer = self.query_player(f'What difficulty of an adventure shall you face?\n{Game.difficulties}')
        if answer in Game.difficulties:
            self.difficulty = answer
            self.diff_scale = Game.difficulties.index(answer) - 2
        else:
            return self.set_difficulty()

    def generate_encounter(self, difficulty):
        # start by calculating the difficulty, this should vary depending on the difficulty chosen by the player.
        true_scaling = difficulty + randint(-1, 1 + self.diff_scale)
        match true_scaling:
            case -1:
                self.query_player('Looks like a relaxed day of traveling...\nPress enter to continue')

    @staticmethod
    def query_player(question:str, clr:bool = True) -> str:
        # This method is the main way of communicating with the player.
        if clr:
            Game.cls()
        answer = input(f'\n{question}\n\n')
        return answer

    @staticmethod
    def cls() -> None:
        # Console clear method... to keep things pretty!
        os.system('cls' if os.name == 'nt' else 'clear')