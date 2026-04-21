"""
NEED TO INPUT A MATRIX AND DO, WILL FINISH
"""
def transpose_matrix(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    transpose_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(ROW):
        for col in range(COL):
            transpose_matrix[col][row] = matrix[row][col]
    return transpose_matrix
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_matrix():
    printing_matrix = transpose_matrix(matrix)
    for row in range(len(printing_matrix)):
        print(f"{printing_matrix[row]}")

def main():
    print_matrix()

main()                   
    



