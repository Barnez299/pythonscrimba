#Sets - Exercise

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends and 'John' in friends)


#2. combine or add the two sets 
print(friends.union(my_friends))

#3. Find names that are in both sets
print(friends.intersection(my_friends))
#4. find names that are only in friends

#5. Show only the names who only appear in one of the lists
print(friends.symmetric_difference(my_friends))
#6. Create a new cars-list without duplicates
cars2 = set(cars)
print(cars2)


# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# print(friends)
# print(friends_tuple)
# print(friends_set)
