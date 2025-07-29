aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Using list comprehension to create aliens
aliens = [{'color': 'green', 'points': 5, 'speed': 'slow'}
          for alien in range(30)]

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
