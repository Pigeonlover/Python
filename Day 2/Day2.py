# Subscripting


# Can use negative number for position, and it will go backwards
print("Hello"[-5]) # Prints last letter

# To write large integers, include _ instead of , to make them easier to read
print(10_500)

# Check data type
print(type(True))

# Convert data type with casting
int("45") # Converts string '45' into an integer
float()
str()
bool()
# Etc... Some things cannot be converted

# "/" gives a float as an answer. "//" gives an integer
8 / 4  # --> 2.0
8 // 4 # --> 2

# "**" for exponential power
2**3  # --> 6


# EXERCISE - BMI CALCULATOR

height = 1.58 
weight = 43.8

bmi = weight / height**2

print(round(bmi))


# F-strings - add 'f' in front of quotes to print; add variables between curly braces {}

print(f"Your BMI is: {bmi}")
