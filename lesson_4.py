# Lists
list_1 = []
i = 0
while i < 5:
    list_1 += [i]
    i +=1

print(list_1)


# using list()

list_2 = list('abc')
print(list_2)


list_3 = list(range(1, 11))
print(list_3)

list_4 = [2.5, 8, 'abc']

for el in list_4:
    print(type(el))

# [index]
print(list_4[0])
print(list_4[-1])

# list.index(element)
print(list_4.index(2.5))

# list.append(element)
list_4.append(8)
print(list_4)

# list.insert((index, element))
list_4.insert(1, 'test')
print(list_4)

# len()
print(len(list_4))

list_copy = list_4
print(list_copy)

# list.copy()

list_copy = list_4.copy()
list_copy = list(list_4)

# list.remove(element)
list_4.remove(8)
print(list_4)

# list.pop(index)
list_4.pop(1)
print(list_4)

list_4.pop()
print(list_4)

del list_4[0]
print(list_4)

# list.clear()
list_4.clear()
print(list_4)

print(list_3)
list_3[2] = 5
list_3[-1] = 12
print(list_3)

# list[start_index: end_index]
print(list_3[0:6])
print(list_3[:6])
print(list_3[6:10])
print(list_3[:])
list_5 = list_3[0:6]
print(list_5)

list_3[0:6] = [0, 0, 0, 0, 0, 0]
print(list_3)
del list_3[0:6]
print(list_3)

# list.extend([list])
list_3.extend([1, 1, 1])
print(list_3)

# list.count(element)
print(list_3.count(1))

print(0 in list_3)

# sorted, sort
sorted_list = sorted(list_3)
print(list_3)

list_3.sort()
print(list_3)

# reverse=True

sorted_list = sorted(list_3, reverse= True)
print(list_3)

list_3.sort(reverse=True)
print(list_3)

# reverse()
print(list_3)
list_3.reverse()
print(list_3)

str_list = ["C", "ABfsdsc", "ab", "BC", "bcd"]
str_list.sort(key=len)
print(str_list)

even_list = list(range(1, 100, 2))
print(even_list)

# max, min, sum
print(max(even_list))
print(min(even_list))
print(sum(even_list))

for element in even_list:
    print(element)

for i in range(len(even_list)):
    print(even_list[i])

# tuple()
tuple_1 = ()
tuple_2 = (1,)
tuple_3 = (1, 2.4, 'abc', 'bcd', 7, 8)


result = False

i = 0
while i < len(tuple_3):
    if tuple_3[i] == 'bcd':
        result = True
        break
    i += 1
if result:
    print("Yes")
else:
    print("No")

print(tuple_3[:3])
tuple_2 = (1, 2, 3)
tuple_4 = tuple_2 + tuple_3
print(tuple_4)
print('abc' in tuple_4)

# tuple.index(element())
print(tuple_4.index(2.4))

print(tuple_4)
for el in tuple_4:
    if el == 'bcd':
        continue
    print(el)

print(tuple_4)
for el in tuple_4:
    if el == 'bcd':
        break
    print(el)

