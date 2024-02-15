from random import randint, sample


def failist_to_dict(f):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []

    try:
        with open(f, 'r', encoding="utf8") as file:
            for line in file:
                parts = line.strip().split('-')
                if len(parts) == 2:
                    k, v = parts
                    riik_pealinn[k.strip()] = v.strip()
                    pealinn_riik[v.strip()] = k.strip()
                    riigid.append(k.strip())
                else:
                    print("Ошибка в строке:", line)

    except FileNotFoundError:
        print("Файл", f, "не найден.")
    return riik_pealinn, pealinn_riik, riigid


def show(riik_pealinn):
    i = 0
    for x in riik_pealinn:
        i += 1
        print(f"{i}: {x} - {riik_pealinn[x]}")
    print()


def save(riik_pealinn):
    with open("Europa.txt", 'w', encoding="utf-8") as f:
        for key, value in riik_pealinn.items():
            f.write(key + "-" + value + "\n")


def game(riik_pealinn):
    win = 0
    max_len = len(list(riik_pealinn.keys()))
    num_questions = 5

    for _ in range(num_questions):
        r = randint(0, max_len - 1)

        if randint(0, 5000) % 2 == 0:
            print("Riik = Pealinn?")
            rp = list(riik_pealinn.keys())[r]
        else:
            print("Pealinn = Riik?")
            rp = list(riik_pealinn.values())[r]

        answer = str(input(f"{rp}=")).capitalize()

        if riik_pealinn[list(riik_pealinn.keys())[r]] == answer or \
           list(riik_pealinn.values())[r] == answer:
            win += 1
            print("Правильно")
        else:
            print("Неверно")

    print(f"Ваш результат: {(win / num_questions) * 100}%")


def find(riik_pealinn):
    sona = input("Введите слово: ").capitalize()

    if sona in riik_pealinn:
        print(f"{sona} -> {riik_pealinn[sona]}")
    elif sona in riik_pealinn.values():
        riik = [key for key, value in riik_pealinn.items() if value == sona][0]
        print(f"{sona} -> {riik}")
    else:
        YN = input("Хотите добавить это слово в словарь? (y/n): ")
        if YN.lower() == "y":
            add(riik_pealinn)


def add(riik_pealinn):
    sona = input("Введите слово: ").capitalize()
    if sona != "":
        riik = ""
        pealinn = ""
        while True:
            option = str(input("R/l: ")).lower()
            if option[0] == "r":
                riik = input("Страна: ").capitalize()
                pealinn = input("Столица: ").capitalize()
                break
            elif option[0] == "l":
                pealinn = input("Столица: ").capitalize()
                riik = input("Страна: ").capitalize()
                break

        print("\nВсе верно?")
        option = input("Введите 'v' для подтверждения, 'q' для выхода: ").lower()
        if option == "v":
            riik_pealinn[riik] = pealinn
        elif option == "q":
            pass
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


def edit(riik_pealinn):
    show(riik_pealinn)
    max_len = len(list(riik_pealinn.keys()))

    while True:
        pick_str = input("Введите номер строки для удаления или 'q' для выхода: ")
        if pick_str.lower() == "q":
            break

        if pick_str.isdigit():
            pick = int(pick_str)
            if 0 < pick <= max_len:
                lrp = list(riik_pealinn.keys())[pick - 1]
                del riik_pealinn[lrp]
                print("Строка", pick, "удалена.")
                break
            else:
                print("Некорректный номер строки.")
        else:
            print("Некорректный ввод. Пожалуйста, введите число или 'q' для выхода.")


riik_pealinn, pealinn_riik, riigid = failist_to_dict("Europa.txt")
