#courses = ['History', 'Math', 'Physics', 'CompSci']
#courses_2 = ['Art' , 'Education']
#print(len(courses))
#print(courses)
#answer: 4
#Answer :['History', 'Math', 'Physics', 'CompSci']

#print(courses[0])
#Answer is History as 0 is the 1st record in our list.

#print(courses[1])
#Answer is HistMathory as 0 is the 2nd record in our list.

#print(courses[-1])
#answer would be CompSci at this will count backwards of the list.

#courses.append('Art')
#['History', 'Math', 'Physics', 'CompSci', 'Art']
#courses.insert(0, 'Art')
#['Art', 'History', 'Math', 'Physics', 'CompSci']

#courses.insert(0, courses_2)
#[['Art', 'Ediucation'], 'History', 'Math', 'Physics', 'CompSci'] - Notice the [] listed as itjust imported the who new list
#courses.extend(courses_2)
#['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education'] - Notice this added the list results to courses

#courses.remove('Math')
#['History', 'Physics', 'CompSci']
#courses.pop()
#['History', 'Math', 'Physics'] - Pop will remove the last entry in the list.

#popped = courses.pop()
#print(popped)
#print(courses)
#CompSci
#['History', 'Math', 'Physics']

# SORTING

#courses.reverse()
#['CompSci', 'Physics', 'Math', 'History']
#courses.sort()
#['CompSci', 'History', 'Math', 'Physics'] - Alphebetiical for sort

#nums = [1, 5, 2, 4, 3]
#nums.sort(reverse=True)
#[5, 4, 3, 2, 1] - How to reverse the order
#print(nums)


#sorted_courses = sorted(courses)
#['CompSci', 'History', 'Math', 'Physics']


#print(sum(nums))

#print(courses)

# to get a True or False statement in the code we can use 'in' to define the result
#print('Art' in courses)
#False
#print('Math' in courses)
#True

#for item in courses:
#    print(item)
# this is creating a look in our list and printing the item. Remember item in this example is a variable
#History
#Math
#Physics
#CompSci

#for courses in enumerate(courses):
#    print(courses)
#(0, 'History')
#(1, 'Math')
#(2, 'Physics')
#(3, 'CompSci')
#This shows the index and the value

#for courses in enumerate(courses, start=1):
#    print(courses)
#(1, 'History')
#(2, 'Math')
#(3, 'Physics')
#(4, 'CompSci')
#This will start your index at 1

#seperate list into a string and how to seperate. 

#courses_str = ', '.join(courses)
#print(courses_str)
#History, Math, Physics, CompSci

#courses_str = ' - '.join(courses)
#print(courses_str)
#History - Math - Physics - CompSci

#new_list = courses_str.split(' - ')

#print(courses_str)
#print(new_list)

#History - Math - Physics - CompSci
#['History', 'Math', 'Physics', 'CompSci']


#TUPLES

#courses = ['History', 'Math', 'Physics', 'CompSci']

# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)
#TypeError: 'tuple' object does not support item assignment
#cant remove or adjust a list with tuples

# Sets - Does not care about order. Sets will also throw out duplicates.
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses.intersection(art_courses))
# #{'History', 'Math'}
# #intersection will comare the 2 sets and provide the shared values. 

# print(cs_courses.difference(art_courses))
# #{'Physics', 'CompSci'}

# print(cs_courses.union(art_courses))
# #{'Physics', 'CompSci', 'Art', 'History', 'Math', 'Design'}

#Creating Empty lists, tuples, sets

# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()