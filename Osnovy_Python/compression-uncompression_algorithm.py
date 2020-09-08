#Использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#https://stepik.org/lesson/3367/step/7?unit=950
s=input()
b=str()
s=s+'1'
c=s[0]
i=0
for r in s:
    if c!=r:
        b+=c+str(i)
        c=r
        i=0
    i+=1
print(b)

#Cжали. Теперь разжимаем.
with open('dataset_3363_2 (1).txt') as inf:
    s1 = inf.readline()
s = ''
print(s1)
count = 0
lencount = 0
i = 0
sold = ''
while i < len(s1):
    if not s1[i].isdigit():

        if s != '':
            for j in range(count):
                print(s,end='')
        s = s1[i]
        count = 0
        lencount = 0
    else:
        count = lencount*count + int(s1[i])
        if lencount == 0: lencount = 1
        lencount = lencount*10
    i += 1
  
print(s)
