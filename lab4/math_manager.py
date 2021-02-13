'''
Модуль построения отношения Парето

===============================
input_json:
{
    "matrix": [
        [3, 1, 2, 4],
        [2, 3, 1, 3]
    ]
}
===============================
output_json:
{
    "answer": [2, 3]
}
===============================
'''

import numpy as np


def solve(json_data):
    '''
    Главный метод. Собирает мапу для jsonify
    '''
    expert_rankings = json_data['matrix']

    n_experts = len(expert_rankings)
    n_alternatives = len(expert_rankings[0])

    # в эту матрицу просуммируются матрицы доминации по экспертам
    dominance_matrix = np.zeros((n_alternatives, n_alternatives))
    for expert_ranking in expert_rankings:
        dominance_matrix += expert_dominance_matrix(expert_ranking)

    # тут соберётся итоговое множество Парето (методом вычёркивания неподходящих)
    pareto = {i + 1 for i in range(n_alternatives)}

    for i, row in enumerate(dominance_matrix):
        # Оптимизация. Если a > b и b > c, то a > c.
        # Другими словами, всё, что мог исключить j-й элемент
        # уже исключил тот элемент, который исключил j-й
        if i + 1 in pareto:
            for j, value in enumerate(row):
                # Сам себя элемент не исключает.
                # Элемент, который и так не в Парето, исключать уже не надо.
                if i == j or not j + 1 in pareto:
                    continue
                # Если все эксперты считают, что одна альтернатива лучше другой,
                # то в матрице доминации будет сумма единичек равная кол-ву экспертов.
                # Если все эксперты считают одну альтернативу лучше другой, то другая
                # исключается из множества Парето.
                # Если хотя бы один считает A>B, а для остальных A=B, то B всё равно исключется.
                if value < n_experts and dominance_matrix[j][i] == n_experts:
                    pareto.remove(i + 1)
                    break
                if value == n_experts and dominance_matrix[j][i] < n_experts:
                    pareto.remove(j + 1)

    return {'answer': list(pareto)}


def expert_dominance_matrix(expert_ranking):
    '''
    Исходя из мест, которые эксперт присвоил элементам,
    можно простроить матрицу доминации по эксперту.
    В матрице 1 на позиции i,j значит, что альтернатива i
    выше в рейтинге, чем альтернатива j
    '''
    n_alternatives = len(expert_ranking)

    dominance_matrix = np.zeros((n_alternatives, n_alternatives))

    for i in range(0, n_alternatives-1):
        for j in range(i+1, n_alternatives):
            # так за наименьшее число проверок можно собрать все единицы
            # (в том числе симметричные относительно главной диагонали)
            if expert_ranking[i] <= expert_ranking[j]:
                dominance_matrix[i][j] = 1
            if expert_ranking[j] <= expert_ranking[i]:
                dominance_matrix[j][i] = 1

    return dominance_matrix
