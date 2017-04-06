planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(['Uranus', 'Neptune'])
planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')
planet_list.append('Pluto')
rocky_planets = planet_list[0:4]
del planet_list[8]

print(planet_list)
print(rocky_planets)

spacecraft_visit = [('Merri', 'Mercury'), ('Lady Gaga', 'Venus'), ('Cassini', 'Saturn')]


for planet in planet_list:
	for craft in spacecraft_visit:
		if planet in craft:
			print(planet+" has been visited by "+str(craft[0]))