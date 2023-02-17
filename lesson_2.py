import math
import random

first_name = "Nikita"
print(id(first_name))

# object: id, type, value

# is, is not

a = 3
b = 5

print(a is b)


print(a is b)

# type()

print(type(a))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a // b)
print(a % b)
print(a**2)

print(8 - 5 + 4/3 * 2**2)


float_value = 5.5315423135
print(round(float_value, 3))

from math import *
from math import sqrt as math_sqrt

# dir()
print(dir(math))
print(math.sqrt(4))

print(dir(random))
# randint
# randrange
# coice

print(random.randint(2, 7))
# from 0 to 14
print(random.randrange(5))

print(random.choice(['python', 'c++', 'c#']))



# strings

demo_string = "Python automation course started"
print(demo_string.title())
print(demo_string.upper())
print(demo_string.lower())

first_name = "Nikita"
last_name = "Piatilietov"
# whitespaces: " ", "\n", "\t"
full_name = first_name + "\n" + last_name
print(full_name)
# rstrip(), lstrip(), strip()

print(full_name.lstrip())

number_string = "1, 23 3,34 5, 6"
replaced_string = number_string.replace(' ', '')
print(replaced_string)

main_string = "this is main string"
sub_string = "main"
print(sub_string in sub_string)

# True is ALL sumbols in lower/upper
print(sub_string.islower())
print(sub_string.isupper())

print(main_string.startswith(sub_string))
print(main_string.endswith(sub_string))

# isalpha()
# only letter
print(sub_string.isalpha())

# letters and numbers
print(sub_string.isalnum())


c = ''
print(c.isdecimal())
print(c.isdigit())

main_string = "a sd as qfr q"
print(main_string.count('a'))
print(main_string.index('a'))

print(len(main_string))
print(main_string.split('_'))


# s1.join(s2)
print("_".join([sub_string, main_string]))

# strint[index]
print(sub_string[-1])

# [n1: n2]
print(sub_string[0: 2])

print(sub_string[::-1])

name = "Nick"
age = 23

# Old style
print("My name is %s, age = %d"%(name, age))

# str.format
print("My name is {0}, age = {1}".format(name, age))

# new style f-string

print(f"My name is {name}, age = {age}")

