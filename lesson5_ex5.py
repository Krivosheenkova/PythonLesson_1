"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('qwe.txt', 'w') as f:
    nums = input('Enter num: ')
    f.write(nums + '\n')
    nums = map(int, nums.split())
    sum_n = sum(nums)
    f.write(str(sum_n))
    print(sum_n)

