#Выведите таблицу размером n x n , заполненную числами от 1 до n^2 спирали
#https://stepik.org/lesson/3369/step/11?unit=952
#Изначальный вариант, который прошел проверку

n = int(input())
i, j = 0, -1
max_j, max_i = n - 1, n - 1
min_j, min_i = 0, 1
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]
while True:
    
    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1
    
    if j == (n - 1) // 2 and i == n // 2:
        break
    
print()
print()
for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end = ' ')
    print()

#Вариант второй, поизящнее.

n = int(input())
for i in range (n):
    for j in range(n):
        k = min (i, j, n - i - 1, n - j - 1)
        if i <= j:
            print (4 * k * (n - k) + j - k + i - k + 1, end = ' ')
        else:
            print (2 * (2 * (n - 2 * k) - 1) + 4 * k * (n - k) - (j - k + i - k + 1), end = ' ')
    print()