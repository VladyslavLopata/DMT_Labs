"""
===================================================
input json:
{
    "alternatives": ["Vasia", "Petia", "Zhora"],
    "states": ["State1", "State2", "State3"],
    "matrix": [
        [1, 2, 3],
        [2, 3, 1],
        [3, 2, 1]
    ]
}
====================================================
output json:
{
    "Laplasus": {
        "A1": {
            "criteria": 4.5,
            "rank": 2
        },
        "A2": {
            "criteria": 4.75,
            "rank": 1
        },
        "A3": {
            "criteria": 4.5,
            "rank": 3
        }
    },
    "Savidge": {
        "A1": {
            "criteria": 6,
            "rank": 2
        },
        "A2": {
            "criteria": 4,
            "rank": 1
        },
        "A3": {
            "criteria": 7,
            "rank": 3
        }
    }
}
====================================================
"""


def savidge(json_data):
    '''
    calculates Savidge method ranking based on input [json_data]
    '''
    matrix = json_data['matrix']

    # максимальные значения по столбцу
    # на ините нули
    max_j = [0 for _ in range(len(matrix[0]))]

    # считаем максимальные по столбцу
    for row in matrix:
        for cell_index, cell in enumerate(row, 0):
            max_j[cell_index] = max(max_j[cell_index], cell)

    # по формуле для каждого элемента считаем значение "жалости"
    # оно равно max_j[j] - matrix[i][j] для всех i, j
    r_matrix = [[max_j[cell_index]-cell_value for cell_index,
                 cell_value in enumerate(row, 0)] for row in matrix]

    # максимальное значение в строке матрицы r - это значение критерия Сэвиджа
    savige_criteria = [max(row) for row in r_matrix]

    # зипуем с названиями альтернатив
    zipped = [i for i in zip(savige_criteria, json_data['alternatives'])]

    # сортируем по возрастанию. Чем меньше значение - тем лучше альтернатива
    zipped.sort(key=lambda x: x[0])

    return zipped


def laplasus(json_data):
    '''
    Calculates Laplasus method ranking based on [json_data]
    '''
    matrix = json_data['matrix']

    row_length = len(matrix[0])

    laplasus_criteria = [sum(row)/row_length for row in matrix]

    # зипуем с названиями альтернатив
    zipped = [i for i in zip(laplasus_criteria, json_data['alternatives'])]

    # сортируем по возрастанию. Чем больше значение - тем лучше альтернатива
    zipped.sort(key=lambda x: x[0], reverse=True)

    return zipped


def solve(json_data):
    '''
    Runs Laplasus and Savidge rankings and returns json answer
    '''
    return {
        "Laplasus": laplasus(json_data),
        "Savidge": savidge(json_data)
    }
