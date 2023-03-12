# task 1


a = int(input("Enter a side: "))
b = int(input("Enter b side: "))
c = int(input("Enter c side: "))
d = int(input("Enter d side: "))


def whats_the_type(a, b, c, d):
    if a == b == c == d:
        print(f"Square: {a},{b},{c},{d}")
    elif a == d or c == b or d == c or d == b:
        print(f"Rectangle space equal: {a * b}")
    else:
        print("Another form")
    return


whats_the_type(a, b, c, d)

# task 2
import random
import secrets
import string

names = ["king", "miller", "kean", "john", "piter"]

domains = ["net", "com", "ua"]

res = ''.join(random.choices(string.ascii_lowercase, k=7))
rand = str(random.randrange(100, 999))


def create_email(domains, names):
    first_part = secrets.choice(names) + "."
    final_email = first_part + rand + "@" + res + "." + secrets.choice(domains)
    print(final_email)
    return


create_email(domains, names)
