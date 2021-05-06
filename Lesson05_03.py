"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32


"""
try:
    with open("Lesson05_03.txt") as f_obj:
        my_dict = {}
        for line in f_obj:
            salary_list = line
            name, salary = salary_list.split()
            my_dict.update({name: float(salary)})
        print("Фамилии сотрудников, чьи зарплаты меньше 20000:")
        for key, value in my_dict.items():
            if value < 20000:
                print(key)
        print(f"Средняя заработная плата сотрудников: {round(sum(my_dict.values()) / len(my_dict.values()),2)}")


except IOError:
    print("Произошла ошибка ввода-вывода!")
