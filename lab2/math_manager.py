'''
{
    "As": ["a1", "a2", "a3", "a4"],
    "Xs": ["x1","x2","x3","x4","x5"],
    "matrix": [
        [1,2,3,4],
        [3,4,5,6],
        [1,2,6,7]
    ]
}
'''


def maxmin(matrix, alternatives):
    minimums = []
    for i in range(0, len(matrix[0])):
        column = []
        for j in range(0, len(matrix)):
            column.append(matrix[j][i])
        minimums.append((min(column), i))

    result = max(minimums, key=lambda tup: tup[0])
    ret_result = (result[0], alternatives[result[1]])
    return ret_result


def maxmax(matrix, alternatives):
    maximums = []
    for i in range(0, len(matrix[0])):
        column = []
        for j in range(0, len(matrix)):
            column.append(matrix[j][i])
        maximums.append((max(column), i))

    result = max(maximums, key=lambda tup: tup[0])
    ret_result = (result[0], alternatives[result[1]])
    return ret_result


def gurvizza(matrix, alternatives, alpha):
    minimums = []
    maximums = []
    for i in range(0, len(matrix[0])):
        column = []
        for j in range(0, len(matrix)):
            column.append(matrix[j][i])
        minimums.append((min(column), i))
        maximums.append((max(column), i))

    results = []
    for i in range(0, len(maximums)):
        results.append(
            ((alpha*maximums[i][0] + (1-alpha)*minimums[i][0]), maximums[i][1]))
    ret = (max(results, key=lambda tup: tup[0])[
           0], alternatives[max(results, key=lambda tup: tup[0])[1]])
    return ret


def solve(json_data):
    a_s = []
    for a in json_data['As']:
        a_s.append(a)

    x_s = []
    for x in json_data['Xs']:
        x_s.append(x)

    matrix = []
    for arow in json_data['matrix']:
        matrix.append(arow)

    results = []

    results.append(maxmin(matrix, a_s))
    results.append(maxmax(matrix, a_s))
    results.append(gurvizza(matrix, a_s, 0.6))
    return results
