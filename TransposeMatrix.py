A=[[5,4,3],
   [2,4,6],
   [4,7,9],
   [8,1,3]]

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i]=A[i][j]
        
print("The transpose of matrix A is : ")
for res in result:
    print(res)