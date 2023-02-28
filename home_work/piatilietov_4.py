# task 1

list_1 = {1, 2, 3, 4, 10, 6, 5}
list_2 = {2, 5, 7, 8, 1, 3, 10}
list_3 = list_1 & list_2
for el in list_3:
    print(el)

# task 2

students = {
    "Ivan": 1,
    "Petro": 6,
    "Helen": 3,
    "Mykyta": 4,
    "Anna": 9
}

avg_grade = sum(students.values()) / len(students)

for students_scr in students.keys():
    if students[students_scr] > avg_grade:
        print(students_scr)

# task 3

list_digits = {1, 3, 5, 6, 65, 23, 5, 5, 10, 3, 5, 6, 11}
new_list = {}
for el in list_digits:
    if el in list_digits:
        del el
print(list_digits)
print(len(list_digits))

# task 4

list_1 = {1, 2, 3, 4, 10, 6, 5}
list_2 = {2, 5, 7, 8, 1, 3, 10}

list_3 = list_1.intersection(list_2)
print(sorted(list_3))

print("First list_1")
for el in list(list_1):
    print(el)

print("Second list_2")
for el in list(list_2):
    print(el)

# task 5

string_test = "one two three one four five seven ten seven one"
splitted_str = string_test.split()
print(splitted_str)
result = set((el, splitted_str.count(el)) for el in splitted_str)
print(result)
