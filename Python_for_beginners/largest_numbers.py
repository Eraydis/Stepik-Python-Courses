# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. 
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

max1 = 0
max2 = 0
n = int(input())
for i in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num     
    elif max2 < num < max1:
            max2 = num                
print(max1)
print(max2, end='\n')
