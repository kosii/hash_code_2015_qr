def evaluate(matrix):
    return min((sum(row) - max(row)) for row in matrix)