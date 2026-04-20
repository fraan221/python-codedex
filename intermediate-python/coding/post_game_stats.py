# Tecnica utilizada: List comprehension

# Esto...
# positions = [player["position"] for player in players_data]

# Es equivalente a esto:
# positions = []
# for player in players_data:
#     positions.append(player["position"])

dataset = [
    {
        "name": "Leandro Paredes",
        "position": "Volante Central",
        "jersey_number": 5,
        "goals": 2,
        "assists": 3,
    },
    {
        "name": "Miguel Merentiel",
        "position": "Delantero Centro",
        "jersey_number": 16,
        "goals": 4,
        "assists": 2,
    },
    {
        "name": "Milton Delgado",
        "position": "Interno Izquierdo",
        "jersey_number": 43,
        "goals": 0,
        "assists": 1,
    },
]

names = [player["name"] for player in dataset]
positions = [player["position"] for player in dataset]

print("Names:", names)
print("Positions:", positions)

# Update
dataset[2]["goals"] += 1

# Average
average_goals = sum(player["goals"] for player in dataset) / len(dataset)

average_assists = sum(player["assists"] for player in dataset) / len(dataset)

print("Average Goals:", average_goals)
print("Average Assists:", average_assists)
