import string
import unittest
from Hangman.Domain.game import Game
from Hangman.Domain.gameState import GameState


class GameTests(unittest.TestCase):
    def test_game_is_singleton(self):
        self.assertEqual(Game._instance, None)
        game = Game()
        self.assertEqual(Game._instance, game)
        game2 = Game()
        self.assertEqual(game, game2)

    def test_guess_only_allow_alpha(self):
        game = Game()
        with self.assertRaises(ValueError):
            game.guess('!')
        with self.assertRaises(ValueError):
            game.guess('1')
        with self.assertRaises(ValueError):
            game.guess(' ')
        with self.assertRaises(ValueError):
            game.guess('')

    def test_guess_raise_error_after_7_fails(self):
        game = Game()
        wrong_letter: chr
        for c in string.ascii_lowercase:
            if not game.word.letters.__contains__(c):
                wrong_letter = c
                break

        for i in range(8):
            game.guess(wrong_letter)

        state = GameState.Lose
        self.assertEqual(state, game.status)

        with self.assertRaises(ValueError):
            game.guess(wrong_letter)

    def test_guess_return_true_if_match(self):
        game = Game()
        correct_letter = game.word.letters[0]
        
        self.assertTrue(game.guess(correct_letter))
        self.assertEqual(7, game.remaining_guesses)


    def test_guess_raise_error_if_game_is_won(self):
        game = Game()
        for c in {l for l in game.word.letters}:
            game.guess(c)

        state = GameState.Win
        self.assertEqual(state, game.status)

        with self.assertRaises(ValueError):
            game.guess('a')



if __name__ == '__main__':
    unittest.main()
