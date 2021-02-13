from lab1.input_manager import get_task_data as gtd
import numpy as np


def solve(json_data):
    # Получить всю инфу
    td = gtd(json_data)

    # Первая строка матрици
    matrix = np.array([td.experts[0].grades], dtype=int)

    # Все остальные строки
    for expert in td.experts[1:]:
        newrow = np.array([expert.grades], dtype=int)
        matrix = np.concatenate((matrix, newrow), axis=0)

    # Сума оценок альтернатив у 1го експерта
    sumy = []
    # Нормированые оценки альтерантив
    finals = []

    # Вычисление суммы оценок альтеранатив
    for row in matrix:
        sumy.append(sum(row))

    # Вычисление нормированых оценок альтернатив
    for column in matrix.transpose():
        a = 0.
        for elem, elemss in zip(column, sumy):
            a += (elem/elemss)
        finals.append(a/len(column))

    return finals
