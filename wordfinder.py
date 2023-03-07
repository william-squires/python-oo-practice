from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Creates a WordFinder with a path to a file with words
           Makes a list with each word in the file as words
           Gets the number of words in the file as num_words"""
        self.file_path = file_path
        self.words = self.get_words_from_file()
        self.num_words = len(self.words)

    def get_words_from_file(self):
        """Gets the words from a file and returns them as a list"""
        words = []
        f_read = open(self.file_path, "r")

        for word in f_read:
            words.append(word[:-1:])

        f_read.close()
        return words
    
    def get_random_word(self):
        return choice(self.words)