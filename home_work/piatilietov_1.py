import math

# task 1
name = input("Enter your name: ")
surname = input("Enter your surname: ")

full_name = name + " " + surname
print(full_name)

result_lower = full_name.lower()
print(result_lower)

result_upper = full_name.upper()
print(result_upper)

result_tittle = full_name.title()
print(result_tittle)

print((full_name + " ") * 5)

splited_str = full_name.split()
new_str = ("\t" + "\t" + splited_str[0] + "\n")
print(new_str)

final_str = new_str.strip()
print(final_str)


# task 2
cercle_rad = int(input("Enter radius of cercle: "))
cercle_length = 2 * math.pi * cercle_rad
cercle_area = math.pi * cercle_rad**2

final_calc = (f"Cercle area equal: {cercle_area}" + "\n"
              + "Cercle length equal: {cercle_length}")
print(final_calc)


# task 3

dollar_course = 39.5
summ = int(input("How much UAH you have?:  "))
convertation = summ / dollar_course
rounded_course = (round(convertation, 2))
print(f"Dollar course is: {dollar_course} UAH ")
print(f"You will get: {rounded_course}$ ")
