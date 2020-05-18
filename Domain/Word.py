class Word:

    def __init__(self, word: str):
        self.letters: [chr] = [c for c in word]

    @property
    def word(self):
        return "".join([c for c in self.letters])

    def __eq__(self, other) -> bool:
        if type(other) == str:
            return self.word == other
        elif type(other) == type(self):
            return self.word == other.word
        else:
            raise ValueError(f"Cannot compare Word with {str(type(other))}")

    def find_letter_occurences(self, char: chr) -> {int}:
        return {i for i in range(len(self.letters)) if self.letters[i] == char}

    def replace_at_indexes(self, indexes: {int}, char: chr):
        for i in indexes:
            self.letters[i] = char
