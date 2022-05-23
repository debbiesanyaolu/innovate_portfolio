music_list = [
    {
        "artist": "Spice Girls",
        "song name": "Wannabe",
        "release year": "1996",
        "genre": "Dance Pop"
    },
    {
        "artist": "Mariah Carey",
        "song name": "All I Want for Christmas Is You",
        "release year": "1994",
        "genre": "Pop"
    },
    {
        "artist": "Michael Jackson",
        "song name": "Man In The Mirror",
        "release year": "1988",
        "genre": "Pop"
    },
    {
        "artist": "Christina Aguilera",
        "song name": "Genie In A Bottle",
        "release year": "1999",
        "genre": "Dance Pop"
    },
]

fave_bands = []

for dict_i in music_list:
    fave_bands.append(list(dict_i.values())[0])

def add_to_list(band):
    fave_bands.append(band)

def del_from_list(band):
    fave_bands.remove(band)

