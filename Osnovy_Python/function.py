#https://stepik.org/lesson/3373/step/7?unit=956
#Условие задачи, которое вынесло мозг :)

dict={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in dict:
        print(dict[x])
    else:
        dict[x]=f(x)
        print(dict[x])
