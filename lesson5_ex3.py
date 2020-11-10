"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить,кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('sal.py') as f:
    all_sal = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' ')
        all_sal.append(int(salary))
        if int(salary) < 20000:
            print(line, end='\n')
    print('Average salary: ', sum(all_sal) / len(all_sal))

