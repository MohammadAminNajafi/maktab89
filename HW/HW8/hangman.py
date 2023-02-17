from random import choice
import re
import requests
import json
import os


def clear():
    os.system('cls' if os.name.lower() == 'nt' else 'clear')


class Bank:
    colours = ['red', 'blue']
    animals = ['dog', 'cat']
    topic_names = ['Colours', 'Animals']
    topics = {'Colours': colours, 'Animals': animals}
    api = 'https://api.api-ninjas.com/v1/randomword'
    api_key = 'FRkfTIwrgLLk+4TIMd+NMA==m6isKOfXzCLPgdGz'

    def __init__(self):
        self.current_topic = ''
        self.current_word = ''
        self.current_word_display = []
        self.letters_guessed_counter = 0
        self.not_solved = True
        self.letters_already_guessed = []

    def pick_topic(self):
        self.current_topic = choice(self.topic_names)
        return f'Topic: {self.current_topic}'

    def get_word(self):
        try:
            response = requests.get(f"{self.api}", headers={'X-Api-Key': f"{self.api_key}"}, params={type: 'noun'})
            if response.status_code == 200:
                word = json.loads(response.text)
                self.api_response_status = True
                self.current_word = word['word']
                for i in self.current_word:
                    self.current_word_display.append('_')
                return f'Word is {len(self.current_word)} letters long.\n {self.current_word_display}'
        except requests.exceptions.ConnectionError:
            self.api_response_status = False

    def pick_word(self):
        self.current_word = choice(self.topics[self.current_topic])
        for i in self.current_word:
            self.current_word_display.append('_')
        return f'Word is {len(self.current_word)} letters long. {self.current_word_display}'

    def check_solve(self):
        self.not_solved = self.letters_guessed_counter < len(self.current_word)


class Player:
    def __init__(self):
        self.lives = 10
        self.answer = ''
        self.guess_validation_incomplete = True

    def guess(self):
        self.answer = input('Guess a letter: ')


class Processes:
    def __init__(self):
        pass

    @staticmethod
    def validate_user_input(player):
        expression = re.match(r'^[a-z]$', player.answer)

        if expression == None:
            return '\nPlease guess a single alphabet'
        player.guess_validation_incomplete = False
        return 'Hangman'

    @staticmethod
    def check_answer_update_lives(bank, player):
        if player.answer in bank.letters_already_guessed:
            return '\nLetter already guessed.'

        elif player.answer not in bank.current_word:
            player.lives -= 1
            bank.letters_already_guessed.append(player.answer)
            return f'\nNope! \nLives remaining: {player.lives}'

        else:
            for i in range(len(bank.current_word)):
                if player.answer == bank.current_word[i]:
                    bank.current_word_display[i] = player.answer
                    bank.letters_guessed_counter += 1
                    bank.letters_already_guessed.append(player.answer)
                    return '\nNice!'

if __name__ == '__main__':
    class Main:
        def __init__(self):
            pass

        while True:
            word_bank = Bank()
            player1 = Player()
            game = Processes()

            print(word_bank.pick_topic())
            word_bank.get_word()
            if  word_bank.api_response_status == True:
                print(word_bank.get_word())

            if word_bank.api_response_status == False:
                print(word_bank.pick_word())
            player1.lives = 3 * len(word_bank.current_word)

            while word_bank.not_solved and player1.lives > 0:
                while player1.guess_validation_incomplete:
                    player1.guess()
                    print(game.validate_user_input(player1))
                    print(game.check_answer_update_lives(word_bank, player1))
                print(word_bank.current_word_display)
                player1.guess_validation_incomplete = True
                word_bank.check_solve()
            # clear()
            if not word_bank.not_solved:
                print('\nYou win!')

            else:
                print('\nYou lose')
                print('Word was {}'.format(word_bank.current_word))

            replay = input('Press any key to play again, x to quit: ')
            print('\n')
            if replay.upper() == 'X':
                break


    Play = Main()
    del Play

