import unittest
from Hangman.Domain.game import Game


class GameTests(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(Game._instance, None)
        game = Game()
        self.assertEqual(Game._instance, game)
        game = Game()



if __name__ == '__main__':
    unittest.main()
