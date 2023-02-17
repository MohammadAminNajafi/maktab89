import unittest
from hangman import Bank, Processes, Player
import requests
from testNetwork import check_ping


class TestBank(unittest.TestCase):
    def setUp(self) -> None:
        self.B = Bank()

    def test_pick_topic(self):
        x = self.B.pick_topic()
        self.assertIn(x, ['Topic: Colours', 'Topic: Animals'])
        self.assertIn(self.B.current_topic, ['Colours', 'Animals'])

    @unittest.skipIf( not check_ping() or requests.get(f"{Bank.api}", headers={'X-Api-Key': f"{Bank.api_key}"}, params={type: 'noun'}).status_code != 200, 'when we connect to internet')
    def test_get_word(self):
        self.B.get_word()
        self.assertEqual(self.B.api_response_status, True)
        self.assertEqual(len(self.B.current_word_display), len(self.B.current_word))
        for i in self.B.current_word_display:
            self.assertEqual(i, '_')

    @unittest.skipIf(check_ping(), 'when we dont connect to internet')
    def test_get_wor(self):
        self.B.get_word()
        self.assertEqual(self.B.api_response_status, False)

    @unittest.skipIf(check_ping(), 'when we dont connect to internet')
    def test_pick_word(self):
        self.B.current_topic = 'Animals'
        self.B.pick_word()
        self.assertIn(self.B.current_word, ['dog', 'cat'])
        self.B.current_topic = 'Colours'
        self.B.pick_word()
        self.assertIn(self.B.current_word, ['red', 'blue'])

    def test_check_solve(self):
        self.B.letters_guessed_counter = 3
        self.B.current_word = 'MANA'
        self.B.check_solve()
        self.assertEqual(self.B.not_solved, True)
        self.B.letters_guessed_counter = 10
        self.B.current_word = 'PEAMAN'
        self.B.check_solve()
        self.assertEqual(self.B.not_solved, False)


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.P = Player()

    def test_init(self):
        self.assertEqual(self.P.lives, 10)
        self.assertEqual(self.P.answer, '')


class TestProcesses(unittest.TestCase):
    def setUp(self) -> None:
        self.P = Processes()
        self.player = Player()
        self.Bank = Bank()

    def test_validate_user_input(self):
        self.player.answer = 'a'
        x = self.P.validate_user_input(self.player)
        self.assertEqual(x, 'Hangman')
        self.player.answer = '2'
        x = self.P.validate_user_input(self.player)
        self.assertEqual(x, '\nPlease guess a single alphabet')

    def test_check_answer_update_lives(self):
        self.player.answer = 'a'
        self.Bank.letters_already_guessed = ['a', 'm']
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertEqual(x, '\nLetter already guessed.')

        self.player.answer = 'v'
        self.Bank.letters_already_guessed = ['y', 'n']
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertNotEqual(x, '\nLetter already guessed.')

        self.player.lives = 2
        self.player.answer = 'b'
        self.Bank.current_word = 'peaman'
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertEqual(x, f'\nNope! \nLives remaining: 1')

        self.player.lives = 4
        self.player.answer = 'b'
        self.Bank.current_word = 'peaman'
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertNotEqual(x, f'\nNope! \nLives remaining: 1')

        self.player.lives = 2
        self.player.answer = 'o'
        self.Bank.current_word = 'peaman'
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertEqual(x, f'\nNope! \nLives remaining: 1')

        self.player.answer = 'e'
        self.Bank.current_word = 'peaman'
        self.Bank.current_word_display = ['_', '_', '_', '_', '_', '_']
        x = self.P.check_answer_update_lives(self.Bank, self.player)
        self.assertEqual(x, '\nNice!')
        self.assertIn(self.player.answer, self.Bank.current_word)


if __name__ == '__main__':
    unittest.main()

