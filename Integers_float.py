#num = 3
#print(type(num))
#PS C:\Users\noxro\Desktop\Python Labs\Testing> & "c:/Users/noxro/Desktop/Python Labs/Testing/venv/Scripts/python.exe" "c:/Users/noxro/Desktop/Python Labs/Testing/Integers.py"
#<class 'int'>

#num = 3.14
#print(type(num))
#PS C:\Users\noxro\Desktop\Python Labs\Testing> & "c:/Users/noxro/Desktop/Python Labs/Testing/venv/Scripts/python.exe" "c:/Users/noxro/Desktop/Python Labs/Testing/Integers.py"
#<class 'float'>

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Floor Division: 3 // 2
#print (3//2)
#This will drop the decimal like it did in previous versions.

# Exponent:       3 ** 2
#print(3**2)
# This is to multiply to the power so in this example 3 is being multiplied to the 2nd power so the answer is 9.

# Modulus:        3 % 2
#print(3 % 2)
# This shows the remainer in a fraction. so the answer would be 1. Example for this is to tell if a number is even or odd

#print(2 % 2)
#print(3 % 2)
#print(4 % 2)
#print(5 % 2)

#PS C:\Users\noxro\Desktop\Python Labs\Testing> & "c:/Users/noxro/Desktop/Python Labs/Testing/venv/Scripts/python.exe" "c:/Users/noxro/Desktop/Python Labs/Testing/Integers_float.py"
#0
#1
#0
#1

#order of operations still gets followed
#print (3 * (2 + 1) ** 2)

#print(abs(-3))
#absolute number (drop the negative). This answer would be 3

#print (round(3.75))
#round up to the nerest whole number answer = 4

#print (round(3.75, 1))
#round to the 1st decimal point answer = 3.8


# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

#num_1 = 3
#num_2 = 2

#print(num_1 == num_2)
#answer is false as the numbers are not equal

#print(num_1 != num_2)
#answer is true as the numbers are not equal

#print(num_1 > num_2)
#answer is true as num_1 is greater than num_2
#.
#.
#.

num_1 = '100'
num_2 = '200'

#print(num_1 + num_2)
#Answer would be 100200 as these ar strings.

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
#answer is now