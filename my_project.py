songs = [
    {'title': 'Legend Has It',
    'artist': 'Run The Jewels',
    'genre': 'Rap',
    'rating': 5
    },

    {'title': 'Highway Queen',
    'artist': 'Nikki Lane',
    'genre': 'Country',
    'rating': 4
    },

    {'title': 'Seven Wonders',
    'artist': 'Fleetwood Mac',
    'genre': 'Classic Rock',
    'rating': 3
    },

    {'title': 'Green River',
    'artist': 'Creedence Clearwater Revival',
    'genre': 'Classic Rock',
    'rating': 2
    },

    {'title': 'Darling',
    'artist': 'Real Estate',
    'genre': 'Indie Rock',
    'rating': 5
    },

    {'title': 'Fire Squad',
    'artist': 'J. Cole',
    'genre': 'Rap',
    'rating': 3
    },

    {'title': 'Cream on Chrome',
    'artist': 'Ratatat',
    'genre': 'Indie Rock',
    'rating': 5
    },

    {'title': 'Life Itself',
    'artist': 'Glass Animals',
    'genre': 'Indie Rock',
    'rating': 4
    },

    {'title': 'Blue Sky',
    'artist': 'Allman Brothers Band',
    'genre': 'Classic Rock',
    'rating': 3
    },

    {'title': 'Angeleno',
    'artist': 'Sam Outlaw',
    'genre': 'Country',
    'rating': 4
    },

    {'title': 'Tamale',
    'artist': 'Tyler, The Creator',
    'genre': 'Rap',
    'rating': 2
    },

    {'title': 'Pulling Teeth',
    'artist': 'Lucius',
    'genre': 'Indie Rock',
    'rating': 5
    },

    {'title': 'Alright',
    'artist': 'Kendrick Lamar',
    'genre': 'Rap',
    'rating': 3
    },

    {'title': 'Brown Sugar',
    'artist': 'The Rolling Stones',
    'genre': 'Classic Rock',
    'rating': 3
    },

    {'title': 'Pure Comedy',
    'artist': 'Father John Misty',
    'genre': 'Indie Rock',
    'rating': 5
    },

    {'title': 'About To Find Out',
    'artist': 'Margo Price',
    'genre': 'Country',
    'rating': 4
    }

    ]

print """
Welcome to your music library
============================
1. View artists
2. View songs
3. View playlists
3. Create playlist
4. Create smart playlist
5. Add songs
6. Delete songs
5. Quit
"""

while True:
    choice = int(raw_input('What do you want to do (1-5)? '))
    if choice == 1:
        for song in songs:
            print song['artist']
    if choice == 2:
        for song in songs:
            print song['title']
    if choice == 3:
        playlist_name = raw_input('Name your playlist: ' )
        song_choice = raw_input('Type the name of the song you wish to add: ')
        for song in songs:
            if song['title'] == song_choice:
                playlist_name.append
                print 'song added'
    if choice == 4:
        song_count = raw_input('How many songs? ')
        genre_spec = raw_input('Favorite genre? ')
