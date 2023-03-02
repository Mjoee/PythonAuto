def add(num1: int, num2: int):
    return num1 + num2


def add_with_default_value(num1, num2=5):
    return num1 + num2


result = add(2, 5)
print(result)

res_2 = add(num2=result, num1=6)

print(add_with_default_value(1, 2))
print(add_with_default_value(1))


def print_demo_text(text, additional=""):
    print(text)
    if additional != "":
        print(text + additional)


def custom_reverse(text: str) -> str:
    tmp_text = ""
    i = len(text) - 1
    while i >= 0:
        tmp_text += text[i]
        i -= 1
    return tmp_text


result = custom_reverse(text="demo text")
print(result)

result = custom_reverse("demo text")
print(result)

n = 4
stepin = 4

if stepin == 1:
    def to_pow(n):
        return n
else:
    if stepin == 2:
        def to_pow(n):
            return n * n

    else:
        def to_pow(n):
            return n ** 3

result = to_pow(1)
print(result)
result_2 = to_pow(2)
print(result_2)
result_3 = to_pow(3)
print(result_3)


def func_name(*args):
    pass


func_name(1, 2, 3, 4, 5)
func_name(1, 2, 3)
func_name()


def make_pizza(*ingridients):
    print(ingridients)


make_pizza("cheese")
make_pizza("cheese", "tomato")
make_pizza("cheese", "tomato", "peperoni")


def build_profile(**user_info):
    for key, value in user_info.items():
        print(f"{key}: {value}")


build_profile(user_name="Nikita", latest_name="Test")
build_profile(user_name="Nikita", latest_name="Test", age=23)


def isPalindrome(inputString: str) -> bool:
    if inputString == inputString[::-1]:
        return True
    return False


text = input("Enter text: ")

is_palindrome = isPalindrome(text)
if is_palindrome:
    print("Is palindrome")
else:
    print("Is not palindrome")


def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b


a, b = swap(3, 4)
print(a)
print(b)


def function1():
    text = "Hello world"

    def function2():
        print(text)

        def function3():
            pass

        function2()


function1()


def recursive_function():
    print("It's recrusive function")
    recursive_function()
# recursive_function()

def factorial(n):
    if n == 1:
        f = 1
    else:
        f = n*factorial(n-1)

    return f

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(10))