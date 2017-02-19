songs = [
    {'title': 'Legend Has It',
    'artist': 'Run The Jewels',
    'genre': 'Rap',
    'year': 2017
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
    print 'Welcome to your music library'
    print '============================'
    print '1. View artists'
    print '2. View songs'
    print '3. View playlists'
    print '4. Create playlist'
    print '5. Create smart playlist'
    print '6. Add songs'
    print '7. Delete songs'
    print '8. Save changes'
    print '9. Quit'

playlists = []
menu_choice = 0
print_menu()
while menu_choice != 9:
    menu_choice = int(raw_input('What do you want to do (1-5)? '))
    if menu_choice == 1:
        for song in songs:
            print song['artist']
    elif menu_choice == 2:
        for song in songs:
            print song['title']
    elif menu_choice == 3:
        print playlists
    elif menu_choice == 4:
        def playlist_name():
            raw_input('Name your playlist: ' )
            song_choice = raw_input('Type the name of the song you wish to add: ')
            for song in songs:
                if song['title'] == song_choice:
                    playlists.append(song_choice)
                    print 'song added'
            #add_another = raw_input('Would you like to add another? (Y or N) ')
            #if add_another == "Y":
                #playlist_name()
            #elif add_another == "N":
                #print_menu()

    elif menu_choice == 5:
        smart_playlist_name = raw_input('Name your smart playlist: ')
        playist_count = raw_input('How many songs in your playlist? ')
        favorite_decade = raw_input('Choose a decade: 60s, 70s, 80s, 90s, 00s, 10s) ')
        favorite_genre = raw_input('Choose a genre ')
    elif menu_choice == 6:
        song_title = raw_input('Song title?: ')
        artist_name = raw_input('Artist name?: ')
        genre = raw_input('genre?: ')
        year = int(raw_input('year?: '))
        new_song = {song_title, artist_name, genre, year}
        songs.extend(new_song)
        print "song added"
    elif menu_choice == 7:
        delete_song = raw_input('What song do you want to delete?')
        if delete_song == songs["title"]:
            del song['title']
    #elif menu_choice == 8:
    elif menu_choice == 9:
        print "Bye."
    elif menu_choice != 5:
        print_menu()
