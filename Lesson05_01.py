"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("text.txt", "w") as f_obj:
    while True:
        temp_input = input("Введите строку")
        if temp_input == "":
            break
        else:
            print(temp_input, file=f_obj)
