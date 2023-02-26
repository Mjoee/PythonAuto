notes = []

while len(notes) != 5 :
    notes.append(input("Enter value: "))
    print(sorted(notes, reverse=True))