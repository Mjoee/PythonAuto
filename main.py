def isinDiapasone(to, isValue, from1=0) -> bool:
    if to >= isValue >= from1:
        return True
    return False


value = int(input("Enter value: "))
to = int(input("Enter to: "))
# from1 = int(input("Enter from: "))

if isinDiapasone(to, value):
    print("Digits in range")
else:
    print("Digits isn't in range")
