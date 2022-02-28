import random

# empty set to store the unique numbers
lotto_set = {}
print(type(lotto_set))
# this has created a dictionary, so use set function to change it
lotto_set = set()
print(type(lotto_set))

# create loop to generate 6 numbers
for i in range(0, 6):
    integer = random.randint(1, 50)
    # add it to your set
    lotto_set.add(integer)

print("Your numbers are:", lotto_set)




