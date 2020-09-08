#Напишите программу, которая считывает три числа.
#Затем выводит на консоль макс. мин. и оставшееся значение
a, b, c  = int(input()), int(input()), int(input())
s = a + b + c;
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))