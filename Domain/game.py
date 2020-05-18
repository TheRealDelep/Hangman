from Hangman.Domain.gameState import GameState
from Hangman.Domain.word_generator import get_random_word
from Hangman.Domain.word import Word


class Game:
    __instance = None

    def __init__(self):
        if Game.__instance is None:
            self.remaining_guesses = 7
            self.status = GameState.Ongoing
            self.word: Word = Word(get_random_word())
            self.masked_word: Word = Word("".join(['_' for c in self.word]))
            Game.__instance = self
        else:
            return Game.__instance


    @property
    def remaining_guesses(self):
        return self._remaining_guesses

    @remaining_guesses.setter
    def remaining_guesses(self, value):
        if value < 0:
            self._remaining_guesses = 0
            self.status = GameState.Lose
        else:
            self._remaining_guesses = value

    @property
    def masked_word(self):
        return self._masked_word

    @masked_word.setter
    def __setitem__(self, key, value):
        self.masked_word[key] = value
        if self.masked_word == self.word:
            self.status = GameState.Win

    def guess(self, char: chr) -> bool:
        if not self.status == GameState.Ongoing:
            raise ValueError("Game is currently not running")
        found_letters = self.word.find_letter_occurences(char)

        if len(found_letters) == 0:
            self.remaining_guesses -= 1
            return False
        else:
            self.masked_word.replace_at_indexes(found_letters, char)
