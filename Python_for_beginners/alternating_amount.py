#На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы 
#
n, s, c = int(input()), 0, 0
for i in range(1,n):
    if i % 2 == 0:
        s += (-i)
    if i % 2 == 1:
        c += i    
d = s+c+(-1)**(n+1)*n
print(d)
