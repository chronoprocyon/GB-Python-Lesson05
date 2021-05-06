"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

try:
    with open("Lesson05_05.txt", "w+") as f_1:
        for i in range(1, random.randint(10, 20)):
            print(random.randint(1, 30), end=" ", file=f_1)
        f_1.seek(0)
        numbers = f_1.readline()
        numbers = [int(x) for x in numbers.split()]
        print(sum(numbers))

except IOError:
    print("Произошла ошибка ввода-вывода!")
