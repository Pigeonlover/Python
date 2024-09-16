import random

# ri = random.randint(1,100) 
# Output can also be a or b
# print(ri)

# ri2 = random.random()
# # Between 0 and 1. Output can be a BUT NOT b
# print(ri2)

# ri3 = random.uniform(1,100)
# # Output can also be a or b
# print(ri3)


# Heads or Tails Challenge
hot = random.randint(0,1) 
if hot == 0:
    print("Heads!")
elif hot == 1:
    print("Tails!")
else:
    ("Error. Please try again.")