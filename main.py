import os
dic_file = {}
directory = r'D:\school\OOP\3\HomeWork\Homework3\file'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f, 'r', encoding='utf-8') as file:
        count = sum(1 for line in file if line.rstrip('\n'))
    with open(f, 'r', encoding='utf-8') as file:
        list = file.read()
        dic_file[filename] = count, list

dic_file_sort = sorted(dic_file.items(), key=lambda x: x[1])

for file_list in dic_file_sort:
    with open('new.txt', 'a', encoding='utf-8') as file:
        file.write(str(file_list[0]))
        file.write('\n')
        for i in file_list[1]:
            file.write(str(i))
            file.write('\n')