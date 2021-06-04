def matrix(size):
    matrix=[]
    for i in range(size):        
        a =[] 
        for j in range(size):      
            a.append(int(input())) 
        matrix.append(a) 
    for i in range(size): 
        for j in range(size): 
            print(matrix[i][j], end = " ") 
        print()
    return matrix
matrix(2)