from scrable_words import scrab, words


sorted_scrab = []
for i in sorted(scrab):
    sorted_scrab.append(i.lower())
sorted_words = []
for j in sorted(words):
    sorted_words.append(j.lower())
with open ('sorted_scrab.py', 'w') as sorted:
    sorted.write('sorted_scrab = ')
    sorted.write(str(sorted_scrab))
    sorted.write('\n')
    sorted.write('sorted_words = ')
    sorted.write(str(sorted_words))