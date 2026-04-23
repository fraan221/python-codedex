from functools import reduce

# List of songs with their durations (in minutes)
playlist = [
    ("What Was I Made For?", 3.42),
    ("Just Like That", 5.05),
    ("Song 3", 6.55),
    ("Leave The Door Open", 4.02),
    ("I Can't Breath", 4.47),
    ("Bad Guy", 3.14),
]


def longer_than_five_minutes(song):
    return song[1] > 5.00


def minutes_to_seconds(song):
    return song[1] * 60


def add_durations(total, song):
    duration = song[1]
    return total + duration


minutes_filter = filter(longer_than_five_minutes, playlist)
print(list(minutes_filter))

convertion_minutes = map(minutes_to_seconds, playlist)
print(list(convertion_minutes))

adding_duration = reduce(add_durations, playlist, 0)
print(adding_duration)
