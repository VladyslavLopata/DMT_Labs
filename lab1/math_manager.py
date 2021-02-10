from input_manager import get_task_data as GTD
import model
import numpy as np


def Solve():
    td = GTD()

    matrix = np.array(td.experts[0].grades)

    for grades in td.experts[1:]:
        np.concatenate(matrix, grades, axis=0)

    sumy = []
    finals = []

    for row in matrix:
        sumy.append(sum(row))


    for column in matrix.transpose():
        a = 0.
        for elem,elemss in zip(column, sumy):
            a += (elem/elemss)
        finals.append(a/len(column))

    return finals

    
