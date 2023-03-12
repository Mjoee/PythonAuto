def func_name():
    pass


# lambda arg_1, arg_2..., arg_n: expression

double = lambda x: x * 2

print(double(6))
print(double(4))
print(double(5))


def to_cube(x):
    return x * x * x


lambda_to_cube = lambda x: x * x * x

print(to_cube(3))
print(lambda_to_cube(3))

lambda_multiple_three_num = lambda a, b, c: a * b * c

res_multiple_three = lambda_multiple_three_num(1, 2, 3)
print(res_multiple_three)

lambda_multiple_two_num = lambda a, b, c: a * b

res_multiple_two = lambda_multiple_three_num(1, 2, 3)
print(res_multiple_two)

import math

sqrt_x = lambda x: math.sqrt(x)
print(sqrt_x(10))

list_a = [1, 2, 3]

import random

lambda_list = [
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
]

for el in lambda_list:
    print(el(5))

lambda_tuple = (
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
)
for el in lambda_tuple:
    print(el("str"))

areas_dictionary = {
    'circle': (lambda r: math.pi * r * r),
    'rectangle': (lambda a, b: a * b),
    'square': (lambda a: a * a)
}

print(areas_dictionary['square'](4))
print(areas_dictionary['rectangle'](1, 2))
print(areas_dictionary['circle'](7))

# filter(), map(), reduce()

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = list(filter(lambda x: x % 2 == 0, list_a))
print(filtered_list)

filtered_list = list(filter(lambda x: x % 2 != 0, list_a))
print(filtered_list)

# map(function, list)
double_list = list(map(lambda x: x * 2, list_a))
print(double_list)

# reduce(function, list)

from functools import reduce

sum = reduce(lambda x, y: x + y, list_a)
print(sum)

list_b = [90, 55, 54, 20, 30]
min_el = reduce(lambda x, y: x if (x < y) else y, list_b)
print(min_el)

generated_list = [lambda x=x: x for x in range(1, 30)]
for el in generated_list:
    print(el())

max_num = lambda x, y: x if x > y else y
print(max_num(7, 6))

list_b = [[12, 12, 2], [23, 4], [43, 24, 2]]
sorted_list = lambda x: (sorted(el) for el in x)
print(list(sorted_list(list_b)))

sum_of_three = lambda a=1, b=2, c=3: a + b + c
print(sum_of_three())
