my_pets = [
    {"kind": "Dog", "owner": "Anna"},
    {"kind": "snake", "owner": "abia"},
    {"kind": "rabbit", "owner": "zarah"},
    {"kind": "Fish", "owner": "ridha"},
]

# Loop through the list and print information about each pet
for pet in my_pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}\n")