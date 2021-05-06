"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

try:
    with open("Lesson05_02.txt") as f_obj:
        lines_list = []
        count = 0
        for line in f_obj:
            count += 1
            words = line.split(' ')
            while words.count(""):
                words.remove("")
            lines_list.append(len(words))
        print(f"Количество строк: {count}")
        for ind, el in enumerate(lines_list, 1):
            print(f"В строке {ind} количество слов: {el}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
