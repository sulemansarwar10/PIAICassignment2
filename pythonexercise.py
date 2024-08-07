#Roll#  PIAIC59391

# 1. Simple Message
# Task: Assign a message to a variable and then print that message.
msg="how are you"
print(msg)
# 2. Simple Messages
# Task:
# ● Assign a message to a variable and print that message.
# ● Change the value of the variable to a new message, and print the new message.
msg="i am fine"
print(msg)
# 3. Personal Message
# Task:
# ● Use a variable to represent a person’s name.
# ● Print a message to that person, such as, “Hello Eric, would you like to learn some
# Python today?”
name="suleman"
print(f"Hello {name}, would you like to learn some Python today?")
# 4. Name Cases
# Task:
# ● Use a variable to represent a person’s name.
# ● Print the person’s name in lowercase, uppercase, and title case.
name='suleman'
print(name.lower())
print(name.upper())
print(name.title())
# 5. Famous Quote
# Task:
# ● Find a quote from a famous person you admire.
# ● Print the quote and the name of its author.
# The output should look something like the following:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”
authername='Albert Einstein'
quote= "A person who never made a mistake never tried anything new."
print(f"{authername} once said, \"{quote}\"")

# 6. Famous Quote 2
# Task:
# ● Use a variable called famous_person to represent the famous person’s name.
# ● Compose the message and represent it with a variable called message.
# ● Print the message.
famous_person="Zia Khan"
message="GenAI is future"
print(f"{famous_person} once said, \"{message}\"")
# 7. Stripping Names
# Task:
# ● Use a variable to represent a person’s name, and include some whitespace characters
# at the beginning and end of the name.
# ● Make sure you use each character combination, \t and \n, at least once.
# ● Print the name once, so the whitespace around the name is displayed.
# ● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
# strip().
person=" suleman \tsarwar "
print(person)
print(person.lstrip())
print(person.rstrip())
print(person.strip())
# 8. Variable Sum
# Task: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
x,y,z=5,10,15
print(x+y+z)
# 9. Variable Swap
# Task: Swap the values of two variables a and b. Print the values before and after the swap.
a="suleman"
b="sarwar"
print("before",a,b)
c=b
b=a
a=c
print("after",a,b)
# 10. Favorite Color
# Task: Create a variable with your favorite color and print it. Then change the variable name to
# something else and print the color again.
color="blue"
print(color)
newcolor="blue"
print(newcolor)
# 11. Changing Pet Name
# Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
# "Max" and print the new value.
pet_name ="Buddy"
pet_name ="Max"
print(pet_name)
# 12. Observing Name Error
# Task: Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
# variable with a different name (like sunsine) and observe the error.
Sunshine="hello"
print(Sunshine)  # NameError: name 'sunsine' is not defined. Did you mean: 'Sunshine'?


# 13. Reassigning Score
# Task: Assign the value 100 to a variable score and print it. Then assign a new value to score
# and print it again.
score=100
print(score)
score=10
print(score)
# 14. City Name
# Task: Create a string variable city and assign it the name of a city you like. Print the city
# name.
city="gujrat"
print(city)
# 15. Title Case Text
# Task: Create a variable text with the value "python programming" and print it in title case.
text="python programming"
print(text.title())
# 16. Lowercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all lowercase letters.
test="Hello, HOW are yOU"
print(test.lower())
# 17. Uppercase Conversion
# Task: Assign a string with mixed cases to a variable and print it in all uppercase letters.
print(test.upper())
# 18. Current Temperature
# Task: Create a variable temperature with the value 25. Print "The current temperature is
# [temperature] degrees." using the variable.
temp=25
print(f"The current temperature is {temp} degrees.")
# 19. Printing a Poem
# Task: Create a variable poem with a short poem that has multiple lines. Print the poem with
# each line starting on a new line.
poem='''Nature's first green is gold,
Her hardest hue to hold.
Her early leaf's a flower;
But only so an hour.
'''
print(poem)