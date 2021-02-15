'''
==============================================
input_json:
{
    "As": ["a1", "a2", "a3", "a4"],
    "Xs": ["x1","x2","x3","x4","x5"],
    "matrix": [
        [1,2,3,4],
        [3,4,5,6],
        [1,2,6,7]
    ]
}
==============================================
output_json:
{
    "gurvizza": [
        [
            4.8,
            "a2"
        ],
        [
            4.6000000000000005,
            "a3"
        ],
        [
            2.8,
            "a1"
        ]
    ],
    "maxmax": [
        [
            7,
            "a3"
        ],
        [
            6,
            "a2"
        ],
        [
            4,
            "a1"
        ]
    ],
    "maxmin": [
        [
            3,
            "a2"
        ],
        [
            1,
            "a1"
        ],
        [
            1,
            "a3"
        ]
    ]
}
==============================================
'''


def common_logics(method, matrix, alternatives):
    '''
    берёт [method] (это или мин или макс по j),
    собирает по нему массив минимумов или максимумов
    соединяет с именами
    сортирует по убыванию
    '''
    minmax = [method(line) for line in matrix]
    named = zip(minmax, alternatives)
    sorted_by_highest = sorted(named, key=lambda x: x[0], reverse=True)
    return sorted_by_highest


def maxmin(matrix, alternatives):
    '''
    Считает критерий Вальда.
    '''
    return common_logics(min, matrix, alternatives)


def maxmax(matrix, alternatives):
    '''
    Считает maxmax
    '''
    return common_logics(max, matrix, alternatives)


def gurvizza(matrix, alternatives, alpha):
    '''
    Берёт максимумы и минимумы по j
    Считает для каждого i формулу с альфой
    Зипует с именами и сортирует по убыванию
    '''
    maxes = [max(line) for line in matrix]
    mins = [min(line) for line in matrix]
    calculated_criteria = [alpha * val[0] +
                           (1-alpha) * val[1] for val in zip(maxes, mins)]
    named = zip(calculated_criteria, alternatives)
    sorted_by_highest = sorted(named, key=lambda x: x[0], reverse=True)
    return sorted_by_highest


def solve(json_data):
    '''
    Парсит жсон
    Собирает ответ
    '''
    a_s = json_data['As']

    matrix = json_data['matrix']

    results = {
        "maxmin": maxmin(matrix, a_s),
        "maxmax": maxmax(matrix, a_s),
        "gurvizza": gurvizza(matrix, a_s, 0.6)
    }

    return results
