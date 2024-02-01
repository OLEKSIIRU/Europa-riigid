

from Function import show, save, game, find, add, edit



def main():
    riik_pealinn_dict, pealinn_riik_dict, riigid_list = failist_to_dict('Europa.txt')
    riik_pealinn = {}  

    while True:
        print("1: Отобразить словарь")
        print("2: Поиск столицы/страны")
        print("3: Добавить слово в словарь")
        print("4: Исправить ошибку в словаре")
        print("5: Проверить знание слов")
        print("6: Сохранить словарь в файл")
        print("0: Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show(riik_pealinn)
        elif choice == "2":
            find(riik_pealinn)
        elif choice == "3":
            word_to_add = input("Введите слово для добавления в словарь: ").capitalize()
            add(riik_pealinn, word_to_add)
        elif choice == "4":
            edit(riik_pealinn)
        elif choice == "5":
            game(riik_pealinn)
        elif choice == "6":
            save(riik_pealinn)
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()

