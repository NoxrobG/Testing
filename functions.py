
# def hello_func():
#         print('Hello Function.') 

# hello_func()
# hello_func()
# hello_func()
# hello_func()


# print('Hello Function.') 
# print('Hello Function.') 
# print('Hello Function.') 
# print('Hello Function.') 

#DRY = DONT REPEAT YOURSELF


# def hello_func(greeting, name = 'You'):
#         return'{}, {}'.format(greeting, name)

# # print(hello_func())

# # print(len('Test'))
# print(hello_func('Hi', 'Corey'))

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}

# student_info(*courses, **info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))