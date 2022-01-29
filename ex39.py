# create a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI",
}

# create a basic set of states and some cities in them
cities = {"CA": "San Fransisco", "MI": "Detroit", "FL": "Jacksonvile"}

# add some more cities
cities["NY"] = "New Yor"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])


# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])


# do ir by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviatied {abbrev}")


# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviatied {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get a abbreviation by state that might not be there
state = states.get("Texas")


if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
