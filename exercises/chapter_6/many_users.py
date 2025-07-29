users = {
    'alice': {
        'first_name': 'Alice',
        'last_name': 'Smith',
        'location': 'New York',
    },
    'bob': {
        'first_name': 'Bob',
        'last_name': 'Johnson',
        'location': 'Los Angeles',
    },
    'charlie': {
        'first_name': 'Charlie',
        'last_name': 'Brown',
        'location': 'Chicago',
    },
}

for username, user_info in users.items():
    full_name = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['location']

    print("\nUsername: " + username)
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
