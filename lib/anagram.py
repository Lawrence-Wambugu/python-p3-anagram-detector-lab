# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        sorted_word = sorted(self.word)
        return [
            candidate for candidate in words
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word
        ]
