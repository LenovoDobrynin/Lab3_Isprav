import random
m = int(input('m = '))
n = int(input('n = '))
A = [ [random.randint(1, 101) for j in range(n)] for i in range(m) ]
B = [ [random.randint(1, 100) for j in range(n)] for i in range(m) ]
res = [[0 for x in range(5)] for y in range(5)]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            res[i][j] += A[i][k] * B[k][j]
print('-------------------------')
print("A:")
for i in range(m):
    print(A[i])
print('B:')
for i in range(m):
    print(B[i])
print('C:')
for i in range(m):
    print(res[i])