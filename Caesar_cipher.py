n = int(input())
a = input()

for i in a:
    k = ord(i)-n
    if k < 97:
        k = k + 26
    print(chr(k), end = '')