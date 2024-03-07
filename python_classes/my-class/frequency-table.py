'''
Generate a frequency table for the ratings list (which is already initialized in the code editor).
Start by creating an empty dictionary named content_ratings.
Loop through the ratings list. For each iteration, complete the following:
If the rating is already in content_ratings, then increment the frequency of that rating by 1.
Else, initialize the rating with a value of 1 inside the content_ratings dictionary.
Print content_ratings
'''
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = []

for i in ratings:
    if i in content_ratings:
        i += 1
    else:
        i = 1
print (content_ratings)
print (ratings)