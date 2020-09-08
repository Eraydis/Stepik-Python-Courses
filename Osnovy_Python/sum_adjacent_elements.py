#Сумма двух соседних чисел.
#Для крайнего элемента соседним является первый элемент списка


a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        print(a[i-1] + a[(i+1)%len(a)], end=' ')
