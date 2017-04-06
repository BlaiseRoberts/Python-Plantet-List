import random

random_numbers = list()

for i in range(19):
	random_numbers.append(random.randrange(50))

print(random_numbers)

squared_numbers = [number*number for number in random_numbers]

print(squared_numbers)