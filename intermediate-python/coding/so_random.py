import random
from functools import reduce

prefixes = ["Mystic", "Golden", "Dark", "Shadow", "Silver"]
suffixes = ["storm", "song", "fire", "blade", "whisper"]


def capitalize_suffix(name):
    return name.capitalize()


capitalization = list(map(capitalize_suffix, suffixes))


def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + " " + random.choice(list_2)


random_names = [create_fantasy_name(prefixes, capitalization) for name in range(10)]


def fire_in_name(name):
    return "Fire" in name


def concatenate_names(name1, name2):
    return name1 + ", " + name2


is_fire_in_name = list(filter(fire_in_name, random_names))
concatenated_names = reduce(concatenate_names, is_fire_in_name)


def display_name_info():
    print("Fantasy Names: ")
    for names in random_names:
        print(names)
    print(f"\nNames with 'Fire': {is_fire_in_name}\n")
    print(f"Names concatenated: {concatenated_names}")


display_name_info()
