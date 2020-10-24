## Responses for bangazonLLC DATA STRUCTURES
planet_list = ["Mercury", "Mars"]

# planet_list.append("Jupiter")
# planet_list.append("Saturn")

planet_list.extend(["Jupiter", "Saturn"])

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

print(planet_list)
rocky_planets = (planet_list[0:4])

print(f'the planet list contains: ', planet_list)

print(f' the rockey planets are: ',rocky_planets)

del planet_list[6]

print(f'the planet list contains: ', planet_list)

# spacecraft list
spacecraft = [
    ("Cassini", "Saturn"),
    ("Viking", "Mars"),
    ("Vega", "Venus")
]

visited = []
str1 = ""

for planet in planet_list:
    #Filter spacecraft list to see if matches planet
    Output = list(filter(lambda x:planet in x, spacecraft))
    if Output:
        visited.append(planet)
        print(f'The only planets visited by spacecraft (in this example) are: ', planet)
str1 = ' '.join(map(str, visited))
print(f'The only planets visited by spacecraft (in this example) are: %s.' % str1)

