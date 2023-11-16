#defining a function
def describe_city(name,country="UAE"):
    print(f'{name} is in {country}')

#Call the function for three different cities
describe_city("sharjah")
describe_city("ajman")
describe_city("fujairah") #This will use new default country value