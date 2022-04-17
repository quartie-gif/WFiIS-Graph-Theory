
def print_matrix(matrix: list):
    '''Function to print a matrix in a nice way'''
    return_string = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            return_string += str(matrix[i][j]) + ' '
        return_string += '\n'
    print(return_string)
