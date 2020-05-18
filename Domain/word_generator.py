import requests
import random


def get_random_word() -> str:
    try:
        with open("word_pool.txt", "r") as word_file:
            words = word_file.readlines()
            return words[random.randint(0, len(words))].strip()
    except IOError:
        __Initialize_word_pool()
        return get_random_word()


def __Initialize_word_pool():
    with open("C:/Users/Delep/PycharmProjects/Hangman/words.txt", "r") as words:
        word_pool = [word for word in words.readlines()
                     if 6 < len(word) < 12]
    # and __is_noun(word.strip())]

    with open("word_pool.txt", "w+") as word_file:
        word_file.writelines(word_pool)


def __is_noun(word: str) -> bool:
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "4e79d43313mshf6ebe45a05c0856p15ec89jsn333a20d1505c"
    }
    response = requests.request("GET", url, headers=headers).json()

    try:
        print(word)
        return response["definitions"][0]["partOfSpeech"] == "noun"
    except:
        return False

