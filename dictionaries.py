
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# student['phone'] = '555-5555'
# student['name'] = 'Jane'
#student.update({'name': 'Jane', 'age': '26', 'phone': '555-5555'})
#del student['age']
#age = student.pop('age')

#print(student)
#print(age)

#print(student.keys())
#dict_keys(['name', 'age', 'courses'])
#print(student.values())
#dict_values(['John', 25, ['Math', 'CompSci']])
#print(student.items())
#dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

for key, value in student.items():
    print(key, value) 

#name John
#age 25
#courses ['Math', 'CompSci']