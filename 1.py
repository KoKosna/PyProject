#GKE1
list = ["Кролик",
        "Волк",
        "Лиса",
        "Слон",
        "Жираф",
        "Дельфин",
        "Кит",
        "Корова",
        "Коза",
        "Хомяк",
        "Тигр",
        "Лев",
        "Олень",
        "Кабан",
        "Медведь",
        "Енот"]
print(list[:])
print("Это хищное животное?")
ans = input()
if ans == 'Да':
    print("Животное относится к семейству кошачьих?")
    ans = input()
    if ans == 'Да':
        print("Есть ли грива?")
        ans = input()
        if ans == 'Да':
            print("Ваш ответ: ",list[11])
        else:
            print("Ваш ответ: ",list[10])
    else:
        print("Может ли быть животное бурого цвета?")
        ans = input()
        if ans == 'Да':
            print("Оно любит мёд?")
            ans = input()
            if ans == 'Да':
                print("Ваш ответ: ",list[14])
            else:
                print("Ваш ответ: ",list[13])
        else:
            print("Оно кусает за бочок?")
            ans = input()
            if ans == 'Да':
                print("Ваш ответ: ",list[1])
            else:
                print("Ваш ответ: ",list[2])

else:
    print("Оно обитает в воде?")
    ans = input()
    if ans == 'Да':
        print("Оно питается планктоном?")
        ans = input()
        if ans == "Да":
            print("Ваш ответ :", list[6])
        else:
            print("Ваш ответ :", list[5])
    else:
        print("Оно живет рядом с человеком?")
        ans = input()
        if ans == 'Да':
            print("Дает молоко?")
            ans = input()
            if ans == 'Да':
                print("Оно мычит?")
                ans = input()
                if ans == 'Да':
                    print("Ваш ответ :", list[7])
                else:
                    print("Ваш ответ :", list[8])
            else:
                print("Длинные уши?")
                ans = input()
                if ans == 'Да':
                    print("Ваш ответ :", list[0])
                else:
                    print("Ваш ответ :", list[9])
        else:
            print("Оно обитает в Африке?")
            ans = input()
            if ans == 'Да':
                print("Длинная шея?")
                ans = input()
                if ans == 'Да':
                    print("Ваш ответ :", list[4])
                else:
                    print("Ваш ответ :", list[3])
            else:
                print("Есть рога?")
                ans = input()
                if ans == 'Да':
                    print("Ваш ответ :", list[12])
                else:
                    print("Ваш ответ :", list[15])