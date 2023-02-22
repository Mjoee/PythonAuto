import datetime

first_date = datetime.datetime.now()
second_date = datetime.datetime(2023, 2, 19)
print(first_date)
print(second_date)

# and, or, not

# true true => false
# true false => false
# false true => false
# false false => false

# or

# true true => true
# true false => true
# false true => true
# false false => false

# not

# true => false
# false => true

print((7 < 10) and (6 < 9))
print((3 < 5) and (16 < 9))
print((3 == 5) or (16 == 16))
print((2 + 2 == 4) and not (2 + 2 == 5) and (2 + 2 == 2 * 2))

while True:
    x = int(input("enter value: "))
    if x < 10:
        print("Value less than 10")
    elif x == 10:
        print("Value equal 10")
    else:
        print("Value more than 10")
