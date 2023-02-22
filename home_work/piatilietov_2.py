import random

# task 1

mIn = random.randint(0, 59)
print(f"Minutes: {mIn}")

if mIn <= 15:
    print("1/4 of hour")
elif 15 < mIn <= 30:
    print("2/4 of hour")
elif 31 <= mIn <= 45:
    print("3/4 of hour")
elif 46 <= mIn <= 59:
    print("4/4 of hour")

# task 2

try:
    birth_date = int(input("Enter your birth month 1-12: "))

    if birth_date <= 2 and birth_date != 0 or birth_date == 12:
        print("You was borned at winter")
    elif 3 <= birth_date <= 5:
        print("You was borned at spring")
    elif 6 <= birth_date <= 8:
        print("You was borned at summer")
    elif 9 <= birth_date <= 11:
        print("You was borned at autumn")
    else:
        print("You entered incorrect value, try again")
except ValueError:
    print('Invalid value')

    # task 3

rand_value = random.randint(0, 999)
print(rand_value)

def getSum(rand_value):
    sum = 0
    for digit in str(rand_value):
        sum += int(digit)
    return sum


sum_value = (getSum(rand_value))

if sum_value % 3 == 0:
    print(f"{rand_value} can be divided by 6")
else:
    print(f"{rand_value} couldn't be divided by 6")

# task 4

coordinate_x = float(input("Enter x: "))
coordinate_y = float(input("Enter y: "))

if coordinate_x > 0 and coordinate_y < 0:
    print("IV")
elif coordinate_x == 0 and coordinate_y < 0:
    print("Coordinate on the line -y ")
elif coordinate_x > 0 and coordinate_y == 0:
    print("Coordinate on the line +x ")
elif coordinate_x < 0 and coordinate_y == 0:
    print("Coordinate on the line -x ")
elif coordinate_x == 0 and coordinate_y > 0:
    print("Coordinate on the line +y ")
elif coordinate_x > 0 and coordinate_y > 0:
    print("I")
elif coordinate_x < 0 and coordinate_y < 0:
    print("III")
elif coordinate_x < 0 and coordinate_y > 0:
    print("II")
else:
    print("Both coordinates equal 0")
