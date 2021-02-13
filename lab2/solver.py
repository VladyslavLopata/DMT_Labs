import json

def maxmin(matrix, alternatives):
    minimums = []
    for i in range(0, len(matrix[0])) :
        column = []
        for j in range(0, len(matrix)) :
            column.append(matrix[j][i])
        minimums.append( (min(column) , i) )  
    
    result = max(minimums, key=lambda tup: tup[0])
    ret_result = (result[0] ,alternatives[result[1]])
    return ret_result

def maxmax(matrix, alternatives):
    maximums = []
    for i in range(0, len(matrix[0])) :
        column = []
        for j in range(0, len(matrix)) :
            column.append(matrix[j][i])
        maximums.append( (max(column) , i) )  
    
    result = max(maximums, key=lambda tup: tup[0])
    ret_result = (result[0] ,alternatives[result[1]])
    return ret_result

def gurvizza(matrix, alternatives, alpha):
    minimums = []
    maximums = []
    for i in range(0, len(matrix[0])) :
        column = []
        for j in range(0, len(matrix)) :
            column.append(matrix[j][i])
        minimums.append( (min(column) , i) )
        maximums.append( (max(column) , i) )
    
    results = []
    for i in range(0, len(maximums)):
        results.append( ( (alpha*maximums[i][0] + (1-alpha)*minimums[i][0] ) , maximums[i][1]) )
    ret = ( max(results, key=lambda tup: tup[0])[0], alternatives[max(results, key=lambda tup: tup[0])[1]] )
    return ret

        

def Solve(json_data):
    As = []
    for A in json_data['As']:
        As.append(A)

    Xs = []
    for X in json_data['Xs']:
        Xs.append(X)

    matrix = []
    for arow in json_data['matrix']:
        matrix.append(arow)
    
    results = []

    results.append(maxmin(matrix, As))
    results.append(maxmax(matrix, As))
    results.append(gurvizza(matrix, As, 0.6))
    return results
