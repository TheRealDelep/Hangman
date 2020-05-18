import unittest
from Hangman.Domain.game import Game


class GameTests(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(Game._instance, None)
        game = Game()
        self.assertEqual(Game._instance, game)
        game2 = Game()
        self.assertEqual(game, game2)



if __name__ == '__main__':
    unittest.main()
