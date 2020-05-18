import unittest
from Domain import Game.Game


class MyTestCase(unittest.TestCase):
    def Game_Is_Singleton(self):
        self.assertEqual(Game.__instance, None)
        game = Game
        self.assertEqual(Game.__instance, game)



if __name__ == '__main__':
    unittest.main()
