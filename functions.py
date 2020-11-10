def greeting(name, age, color='red'):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print(f'Hello {name.title()}, you are {age}!. Your favorite color is {color} and you will be {age_next_bday} years old in a years time.')

name = input('Enter your name: ')
age = input('Enter your age: ')
age_next_bday = int(age) + 1
color = input('What is your favourite color: ')
greeting(name, age, color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 