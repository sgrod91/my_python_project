songs = [
    {'title': 'Legend Has It',
    'artist': 'Run The Jewels',
    'genre': 'Rap',
    'year': 2016
    },

    {'title': 'Highway Queen',
    'artist': 'Nikki Lane',
    'genre': 'Country',
    'year': 2017
    },

    {'title': 'Seven Wonders',
    'artist': 'Fleetwood Mac',
    'genre': 'Classic Rock',
    'year': 1987
    },

    {'title': 'Green River',
    'artist': 'Creedence Clearwater Revival',
    'genre': 'Classic Rock',
    'year': 1969
    },

    {'title': 'Loser',
    'artist': 'Beck',
    'genre': 'Indie Rock',
    'year': 1994
    },

    {'title': 'Straight Outta Compton',
    'artist': 'NWA',
    'genre': 'Rap',
    'year': 1988
    },

    {'title': "Lover I Don't Have To Love",
    'artist': 'Bright Eyes',
    'genre': 'Indie Rock',
    'year': 2002
    },

    {'title': 'Oxford Comma',
    'artist': 'Vampire Weekend',
    'genre': 'Indie Rock',
    'year': 2008
    },

    {'title': 'Blue Sky',
    'artist': 'Allman Brothers Band',
    'genre': 'Classic Rock',
    'year': 1972
    },

    {'title': 'Turtles All The Way Down',
    'artist': 'Sturgill Simpson',
    'genre': 'Country',
    'year': 2014
    },

    {'title': 'Tamale',
    'artist': 'Tyler, The Creator',
    'genre': 'Rap',
    'year': 2013
    },

    {'title': 'Sunday Morning',
    'artist': 'The Velvet Underground',
    'genre': 'Classic Rock',
    'year': 1967
    },

    {'title': 'Alright',
    'artist': 'Kendrick Lamar',
    'genre': 'Rap',
    'year': 2015
    },

    {'title': 'Brown Sugar',
    'artist': 'The Rolling Stones',
    'genre': 'Classic Rock',
    'year': 1971
    },

    {'title': 'Where Is My Mind?',
    'artist': 'Pixies',
    'genre': 'Indie Rock',
    'year': 1988
    },

    {'title': 'Fast As You',
    'artist': 'Dwight Yoakam',
    'genre': 'Country',
    'year': 1993
    }
]


def print_menu():
    print('Welcome to your music library\n'\
    '============================\n'\
    '1. View artists\n'\
    '2. View songs\n'\
    '3. View playlists\n'\
    '4. Create playlist\n'\
    '5. Add songs\n'\
    '6. Delete songs\n'\
    '7. Quit')

def _handle_show_artists():
    for song in songs:
        print(song['artist'])

def _handle_show_title():
    for song in songs:
        print(song['title'])

def _handle_add_songs():
    song_title = raw_input('Song title?: ')
    artist_name = raw_input('Artist name?: ')
    genre = raw_input('Genre?: ')
    year = int(raw_input('year?: '))
    new_song = {'title': song_title,
                'artist': artist_name,
                'genre': genre,
                'year': year}
    songs.append(new_song)
    print('song added')


playlists = {'my dope ass rap playlist': [{'title': 'Legend Has It',
                                           'artist': 'Run the Jewels',
                                           'year': 2017,
                                           'genre': 'Rap'}]
            }
menu_choice = 0
while menu_choice != 7:
    print_menu()
    menu_choice = int(raw_input('What do you want to do (1-7)? '))
    if menu_choice == 0:
        print(songs)
    elif menu_choice == 1:
        _handle_show_artists()

    elif menu_choice == 2:
        _handle_show_title()

    elif menu_choice == 3:
        print(playlists)

    elif menu_choice == 4:
        playlist_name = raw_input('Playlist name: ')
        song_title = raw_input('Song title?: ')
        artist_name = raw_input('Artist name?: ')
        genre = raw_input('Genre?: ')
        year = int(raw_input('year?: '))
        new_playlist = {playlist_name: [{'title': song_title,
                                         'artist': artist_name,
                                         'year': year,
                                         'genre': genre}]
                    }
        playlists.update(new_playlist)
        print('playlist added')

    elif menu_choice == 5:
        _handle_add_songs()
    elif menu_choice == 6:
        delete_song = raw_input('What song do you want to delete? ')
        for index, song in enumerate(songs):
            if song['title'] == delete_song:
                del songs[index]
                break
    elif menu_choice == 7:
        print('Bye.')
    elif menu_choice != 5:
        print_menu()




#playlists should be a DICTIONARY

