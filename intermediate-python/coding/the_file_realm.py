liked_songs = {
    "Together Forever": "Rick Astley",
    "Paradise": "Sade",
    "Mystery Man": "The Outfield",
    "Maneater": "Daryl Hall & John Oates",
    "Young Turks": "Rod Stewart",
}


def write_liked_songs_to_file(liked_songs, file_name):
    with open(f"{file_name}.txt", "w") as ls:
        ls.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            ls.write(f"{song} by {artist}\n")


write_liked_songs_to_file(liked_songs, "liked_songs")
