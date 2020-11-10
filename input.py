# using client input



# name = input('what is your name?: ')
# surname = input('what is your surname?: ')
# current_year = int(input('please enter current year: '))
# year_born = int(input('please enter the year you were born in: '))
# age = current_year - year_born

# print(f'Hello {name.capitalize()} {surname.capitalize()} you are currently {age} years old')

# write a program that converts - kms to miles

name = input('please enter your name to start: ')
current_kms = float(input('please enter total km\'s: '))
miles = 1.609
total_kms = float(current_kms / miles)
print(f'Good day {name.capitalize()} {current_kms} km\'s = {round(total_kms,1)} miles')