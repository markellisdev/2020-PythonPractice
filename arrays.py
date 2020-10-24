import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

print(my_randoms)

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    for random in my_randoms:
        if number == random:
            print(f'{number} is in the random list')
    the_numbers_match = False

my_randoms

DVDCollection = []

class DVD(object):
    """
    name = {}
    releaseYear = {}
    director = {}
    """
    pass

newDVD = DVD()