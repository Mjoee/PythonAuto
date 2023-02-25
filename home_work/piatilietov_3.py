notes = []

while True:
    action = input("Enter action (add/earliest/latest/longest/shortest/Exit): ")

    if action == "add":
        note = input("Enter note: ")
        notes.append(note)
        print("Note added.")

    elif action == "earliest":
        sorted_notes = sorted(notes)
        print("Notes (earliest to latest):")
        for note in sorted_notes:
            print(note)

    elif action == "latest":
        sorted_notes = sorted(notes, reverse=True)
        print("Notes (latest to earliest):")
        for note in sorted_notes:
            print(note)

    elif action == "longest":
        sorted_notes = sorted(notes, key=len, reverse=True)
        print("Notes (longest to shortest):")
        for note in sorted_notes:
            print(note)

    elif action == "shortest":
        sorted_notes = sorted(notes, key=len)
        print("Notes (shortest to longest):")
        for note in sorted_notes:
            print(note)

    elif action == "Exit":
        print("Exiting program.")
        break

    else:
        print("Invalid action. Please try again.")
