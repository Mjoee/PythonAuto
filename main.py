list_1 = [22, 22, 53, 43, 12, 42]
test_1 = lambda x: x % 2 == 0
filtered_list = list(filter(test_1, list_1))
print(len(filtered_list))

filtered_list2 = list(filter(lambda x: x % 2 != 0, list_1))
print(len(filtered_list2))
