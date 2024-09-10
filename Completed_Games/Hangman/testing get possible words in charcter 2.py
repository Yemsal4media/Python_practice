from words_list import scrable, simple_words, oxford
from english_words import get_english_words_set
import os

word_array = list(get_english_words_set(["web2"], lower=True))
for char in word_array:
    if len(char) <= 3:
        print(char, end=' ')
''' 
word = input('Enter the word: ')
new_word = []
for i in word:
    new_word.append(i)
print(new_word)

subset = []
for word in scrable:
    new_words = []
    for char in word:
        while char in new_word:
            new_words.append(word)
print(new_words)
'''