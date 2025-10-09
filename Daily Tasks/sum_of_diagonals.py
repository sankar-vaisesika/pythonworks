#sum of diagonals

X=[[1,3],
    [3,4]]

Y=0

for i in range(len(X)):
    for j in range(len(X)):
        if i==j:

            Y+=X[i][j]

print(Y)
