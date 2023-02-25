# создание списка
notes = []
# создание цикла
while True:
    # ввод экшена
    action = input("Enter action (add/earliest/latest/longest/shortest/Exit): ")

    # добавление элемента в список
    if action == "add":
        note = input("Enter note: ")
        notes.append(note)
        print("Note added.")
    # сортировка от старой к новой
    elif action == "earliest":
        sorted_notes = sorted(notes)
        print("Notes (earliest to latest):")
        for note in sorted_notes:
            print(note)
    # сортировка от новой к старой
    elif action == "latest":
        sorted_notes = sorted(notes, reverse=True)
        print("Notes (latest to earliest):")
        for note in sorted_notes:
            print(note)
    # сортировка с длинного по короткий
    elif action == "longest":
        sorted_notes = sorted(notes, key=len, reverse=True)
        print("Notes (longest to shortest):")
        for note in sorted_notes:
            print(note)
    # сортировка с короткого по длинный
    elif action == "shortest":
        sorted_notes = sorted(notes, key=len)
        print("Notes (shortest to longest):")
        for note in sorted_notes:
            print(note)
    # если вводим Exit то сработает break
    elif action == "Exit":
        print("Exiting program.")
        break
    # если вводится что-то другое падаем в елсе и идем по кругу
    else:
        print("Invalid action. Please try again.")
