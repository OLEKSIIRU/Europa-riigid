from random import *

def failist_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding="utf8")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik=[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid


def show():
    i = 0
    for x in riik_pealinn:
        i += 1
        print(f"{i}: {x} - {riik_pealinn[x]}")

    print()

def save():
    max_len = len(list(riik_pealinn.keys()))
    with open("Europa.txt", 'w') as f:
        f.write("")
    
    with open("Europa.txt", 'a') as f:
        for x in range(max_len):
            f.write(f"{list(riik_pealinn.keys())[x]}-{list(riik_pealinn.values())[x]}\n")

def game():
    win = 0
    max_len = len(list(riik_pealinn.keys()))
    
    for x in range(max_len):
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

    print(f"{(win / max_len) * 100}% ваш результат")
    print()

def find():
    sona = str(input("Введите слово: ")).capitalize()

    if sona in riik_pealinn:
        print(f"{sona} -> {riik_pealinn[sona]}")
    elif sona in riik_pealinn.values():
        
        riik = [key for key, value in riik_pealinn.items() if value == sona][0]
        print(f"{sona} -> {riik}")
    else:
        YN = str(input("Хотите добавить это слово в словарь? (y/n): "))
        if YN[0].lower() == "y":
            add(sona)

def add(sona):
    if sona != "":
        while True:
            option = str(input("R/l: ")).lower()
            if option[0] == "r":
                r = sona
                break
            elif option[0] == "l":
                l = sona
                break

        while True:
            if option[0] != "r":
                riik = str(input("Страна?: ")).capitalize()
            elif option[0] != "l":
                pealinn = str(input("Столица: ")).capitalize()
            print("\nВсе верно?")
            option = input("Введите 'v' для подтверждения, 'q' для выхода: ").lower()
            if option == "v":
                riik_pealinn[riik] = pealinn
                break
            elif option == "q":
                break

def edit():
    show()
    max_len = len(list(riik_pealinn.keys()))
    pick = 0
    while not (0 < pick <= max_len):
        pick1 = str(input("Строка: "))
        if pick1[0].lower() == "q":
            break
        if pick1.isnumeric():
            pick = int(pick1)

    lrp = list(riik_pealinn.keys())[pick - 1]
    op = str(input("Тест: ")).capitalize()
    while True:
        if op[0].lower() == 'l':
            nimi = str(input("Тест: ")).capitalize()
            riik_pealinn[lrp] = nimi
            break
        elif op[0].lower() == 'r':
            riik = str(input("Страна: ")).capitalize()
            break
