rivers = {
    'rhine': 'germany',
    'volga': 'russia',
    'yangtze': 'china'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Print the names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)