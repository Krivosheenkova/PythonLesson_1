"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def get_param(name,
              surname,
              year,
              city,
              email,
              phone):
    print(name,
          surname,
          year,
          city,
          email,
          phone)


get_param(name=input('Enter your name: '),
          surname=input('Enter your surname: '),
          year=input('Enter the year you were born: '),
          city=input('Enter the city you live in: '),
          email=input('Enter your email: '),
          phone=input('Enter your phone number: '))
