from words_list import scrable

dictionary = scrable
# ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run', 'balm', 'blame', 'glam']

character = []

word = input('Enter word to find_')
for i in word:
    character.append(i)
print(character)

def find_words(dictionary, character, word=''):
    if word in dictionary:
        print(word, end=' ')

    for char in character:
        new_character = character.copy()
        new_character.remove(char)
        find_words(dictionary, new_character, word + char)
find_words(dictionary, character)