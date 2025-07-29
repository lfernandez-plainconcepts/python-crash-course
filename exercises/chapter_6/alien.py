alien = {'color': 'green', 'points': 5}

print(alien['color'])
print(alien['points'])

print(alien)
alien_1 = {'color': 'yellow', 'points': 10}

# This will raise a KeyError since 'origin_planet' does not exist
# del alien_1['origin_planet']

language_favs = {
    'alice': 'c#',
    'bob': 'python',
    'carmen': 'typescript',
}

my_favorite_language = language_favs.get('luis', 'c#')


my_favorite_language = language_favs.get('luis')
print(my_favorite_language)


# Looping over KVPs
for key, value in alien.items():
	print(f"{key} -> {value}")

# Looping over keys (default behaviour)
for key in alien.keys():	
	print(f"{key} -> {alien[key]}")

for key in alien:	
	print(f"{key} -> {alien[key]}")