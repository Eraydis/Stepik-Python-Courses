
#Найти самое часто используемое слово в датасете


with open('dataset_3363_3.txt', 'r') as inf:
    words_line = []
    for line in inf:
        words_line += line.strip().split()    
dict = {}
for word in words_line:
    for key in dict:
        if word.lower() == key.lower():
            dict[key] += 1
            break
    else:
        dict[word] = 1
str_max = ''
num_str_max = 0
for key in dict.keys():
    if dict[key] > num_str_max:
        num_str_max = dict[key]
        str_max = key
    elif dict[key] == num_str_max:
        if key < str_max:
            str_max = key
print(str_max, num_str_max