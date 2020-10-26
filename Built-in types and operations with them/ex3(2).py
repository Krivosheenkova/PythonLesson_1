# Ex. 3
#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и через dict
season = {'Winter': (1, 2, 12),
          'Spring': (3, 4, 5),
          'Summer': (6, 7, 8),
          'Autumn': (9, 10, 11)}
try:
    month = int(input('Enter number of month: '))
    for key in season.keys():
        if month in season[key]:
            print(key)
except ValueError:
    print('Wrong value!')
if 1 < month > 12:
    print("Wrong value! Expected 1-12")
# season_list = ['0', 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer',
#                'Autumn', 'Autumn',
#                'Autumn', 'Winter']
# try:
#     month = int(input('Enter the number of month: '))
#     for el in season_list:
#         month = season_list.index(el)
#     if month in season_list:
#         print(season_list.index(el))
# except ValueError:
#     print('Wrong!')
