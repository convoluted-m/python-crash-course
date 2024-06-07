# Use remove() function in a while loop to remove all instances of a specific value from a list

# original list
poetry_genres = ['ode', 'allegory', 'ballad', 'epic', 'elegy', 'epitah', 'fable', 'haiku','hymn', 'lyric', 'ode',  'prose poetry', 'satire', 'ode', 'sonnet'] 
print(poetry_genres)
print(len(poetry_genres))

# remove the repeated values
while 'ode' in poetry_genres:
    poetry_genres.remove('ode')

print(poetry_genres)
print(len(poetry_genres))