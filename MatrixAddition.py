
X = [[10,7,3],
    [3 ,5,9],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,3,3],
    [4,7,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
