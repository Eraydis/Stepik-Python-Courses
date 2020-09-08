
#Посчитать количество строк в датасете с помощью модуля requests


import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/764.txt')
x = r.text
print(len(x.splitlines()))