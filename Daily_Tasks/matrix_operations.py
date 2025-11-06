# Matrix Operations (Addition, Multiplication, Transpose)

def matrix_addition(a,b):
    
    if len(a)!=len(b) or len(a[0])!=len(b[0]):

        return "Operation not possible"
    
    result=[]
    for i in range(len(a)):
        row=[]

        for j in range(len(b[0])):

            row.append(a[i][j]+b[i][j])
        result.append(row)
    return result

             


def transpose_matrix(a):       
    result=[]
    for i in range(len(a[0])):
        row=[]
        for j in range(len(a)):
            row.append(a[j][i])
        result.append(row)

    return result

def matrix_multiply(a,b):

    if len(a[0])!=len(b):
        return "Multiplication is not possible"
    
    result=[]

    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            total=0
            for k in range(len(b)):
                total+=a[i][k]*b[k][j]

            row.append(total)
        result.append(row)


    return result


a = [[1, 2],    
     [3, 4]]

b = [[5, 6],
     [7, 8]]

print("a + b =", matrix_addition(a, b))
print("Transpose of a =", transpose_matrix(a))
print("Multiple of a*b =",matrix_multiply(a,b))