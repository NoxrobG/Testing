greeting = "Hello"
name = "Rob"

#one way to write this:
#message = greeting + ", " + name + ". Welcome!"

#possibly easier way to right this
#message = "{}, {}. Welcome!".format(greeting,name)

#using format strings to make it even easier.
#.lower = make this all lower case
#.upper = make this all upper case

message = f"{greeting.upper()}, {name.lower()}. Welcome!"

print(message)


#To see all the varibles for the sting:
#print((dir(name)))

#Returns the following: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', 
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
#'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#This will give you helpful information about the method being asking (in this case the string (str))
#print(help(str))

#Another Example:
#print(help(str.lower))
#Returned: 
# lower(self, /) unbound builtins.str method
# Return a copy of the string converted to lowercase.

