def num_days():

    month = input('Please select month: ')
    feb_28 = ['feb']
    days_30 = ['march', 'jun','sep', 'nov']
    days_31 = ['jan', 'april', 'may', 'july', 'august', 'oct', 'dec']

    if month in days_30:
        print('Number of days = 30 days')

    elif month in days_31:
        print('Number of days = 31 days')

    elif month in feb_28:
        print("Feb only has 28 days and 29 days in a leap year")

    else:
        print('invalid selection')

    # if month == 'jan':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'apr':
    #     print('number of days in',month,'is',30)
    # elif month == 'may':
    #     print('number of days in',month,'is',31)
    # elif month == 'jun':
    #     print('number of days in',month,'is',30)
    # elif month == 'jul':
    #     print('number of days in',month,'is',31)
    # elif month == 'aug':
    #     print('number of days in',month,'is',31)
    # elif month == 'sep':
    #     print('number of days in',month,'is',30)
    # elif month == 'oct':
    #     print('number of days in',month,'is',31)
    # elif month == 'nov':
    #     print('number of days in',month,'is',30)
    # elif month == 'dec':
    #     print('number of days in',month,'is',31)

num_days()