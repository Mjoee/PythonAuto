# create set

firt_set = set(['a', 5, 1.23])
print(type(firt_set))

second_set = {0, 1, 2, 3, 4, 5}
print(type(second_set))

# {'H', 'e', 'l', 'o'}
third_set = set("Hello")
print(third_set)

# in, not in, -, |, &, ^

demo_set = {3, 8, 'a', 'b', "hello"}
element = {'a', 'b', 'c'}

if element in demo_set:
    print("The element is in set")
else:
    print("The element doesn't in set")

# set1 - set2 -> set1.difference(set2)

s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 8, 9}
s3 = s1 - s2
print(s3)
print(s1.difference(s2))

# ser1 | set2 -> s1.union(s2)

s3 = s1 | s2
print(s3)
print(s1.union(s2))

# set1 & set2 -> s1.set1.intersection(set2)

s3 = s1 & s2
print(s3)
print(s1.intersection(s2))

# set1 ^ set2 -> set1.symeric_difference(set2)
s3 = s1 ^ s2
print(s3)
print(s1.symmetric_difference(s2))

# set1.issubset(set2)
print(s1.issubset(s2))

# set1.issuperset(s2)
print(s1.issuperset(s2))

# len(set)
print(len(s1))

# set.copy()
s4 = s1.copy()
print(s4)

demo_list = [5, 3, 2, 6, 8, 9, 0, 1, 2, 3]
filter_set = list(set(demo_list))
print(filter_set)

#  set1 > set2,  set1 >= set2

x = {1, 2, 3, 4}
y = {1, 2}
print(x > y)
y = {1, 2, 3, 4}
print(x >= y)

# set1 < set2, set1 <= set2

x = {1, 2, 3, 4}
y = {1, 2, 3, 4, 8, 9}
print(x < y)

# set.add(element)

x.add("hello")
x.add(8)
x.add(False)
x.add(8.9)
print(x)

# set.remove(element)
x.remove(4)
print(x)

# set.discard(element)
x.discard(3)
x.discard(5)
print(x)

# set.pop()
print(x.pop())
print(x)

# set.clear()
x.clear()
print(x)

# dictionary -> {key: value}

dict_1 = {}
dict_1 = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
print(dict_1)
print(dict_1[2])
print(dict_1)

dict_2 = dict(Monday=1, Tuesday=2, Wednesday=3, Thursday=4, Friday=5)
print(dict_2)
dict_2[7] = "Sunday"
print(dict_2)
dict_2[7] = "Sund"

dict_1 = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
dict_2 = {6: "Saturday", 5: "Friday"}

# dict_1.update(dict_2)

dict_1.update(dict_2)
print(dict_1)

# del
# del dict_2[1]
print(dict_2)

# clear()
dict_1.clear()
print(dict_1)

# dict = {}
dict_1 = {}
print(dict_1)

# in not in

print(dict_1)
print(6 in dict_1)
print(9 not in dict_1)

# dict.get(key, optional_value)
print(dict_1.get(2))
print(dict_2.get(1, "Monday"))

# dict.keys()

print(list(dict_2.keys()))

# dict.values()
print(dict_2.values())

# dict.items()
print(list(dict_2.items()))

# dict.setdefault(key, value)
dict_2.setdefault(1, "Monday")
print(dict_2)

# for
for el in dict_2.keys():
    print(el)

for el in dict_2.values():
    print(el)

for key, value in dict_2.items():
    print(key, value)

# zip()

list_key = [1, 2, 3]
list_values = ["Value1", "value2", "value3"]

generated_dict = dict(zip(list_key, list_values))
print(generated_dict)


