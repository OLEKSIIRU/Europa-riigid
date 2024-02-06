

from Function import show, save, game, find, add, edit, failist_to_dict

def main():
    riik_pealinn_dict, pealinn_riik_dict, riigid_list = failist_to_dict('Europa.txt')

    while True:
        print("1: Отобразить словарь")
        print("2: Поиск столицы/страны")
        print("3: Добавить слово в словарь")
        print("4: Удалить строку в словаре")
        print("5: Проверить знание слов")
        print("6: Сохранить словарь в файл")
        print("0: Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show(riik_pealinn_dict)
        elif choice == "2":
            find(riik_pealinn_dict)
        elif choice == "3":
            word_to_add = {}
            add(riik_pealinn_dict, word_to_add)

        elif choice == "4":
            edit(riik_pealinn_dict)
        elif choice == "5":
            game(riik_pealinn_dict)
        elif choice == "6":
            save(riik_pealinn_dict)
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
