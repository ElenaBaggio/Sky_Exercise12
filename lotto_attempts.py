import random

# using list instead of set
lotto_list = []
print(type(lotto_list))

for i in range(0, 6):
    integer = random.randint(1, 50)
    # to make it unique
    while integer in lotto_list:
        integer = random.randint(1, 50)
    lotto_list.append(integer)

print("Your lotto numbers are:", lotto_list)





