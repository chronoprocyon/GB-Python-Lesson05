"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

try:
    with open("Lesson05_07.txt") as f_obj:
        average_profit = []
        dict_firm = {}
        for line in f_obj:
            line = line.split(" ")
            profit = int(line[2]) - int(line[3])
            if profit > 0:
                average_profit.append(profit)
            dict_firm.update({line[0]: profit})
        average_profit = sum(average_profit) / len(average_profit)
        dict_profit = {"average_profit": average_profit}
        union = [dict_firm, dict_profit]
        with open("Lesson05_07.json", "w") as write_f:
            json.dump(union, write_f)

except IOError:
    print("Произошла ошибка ввода-вывода!")
