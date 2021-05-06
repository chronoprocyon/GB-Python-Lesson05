"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""
try:
    with open("Lesson05_04.txt") as f_1:
        with open("Lesson05_04_out.txt", "w") as f_2:
            my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
            for line in f_1:
                for key, value in my_dict.items():
                    if line.startswith(key):
                        line = line.replace(key, value)
                        print(line, file=f_2)
except IOError:
    print("Произошла ошибка ввода-вывода!")
