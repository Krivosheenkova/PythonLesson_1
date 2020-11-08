"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def f_division(*args):
    try:
        arg1 = float(input('Enter dividend: '))
        arg2 = float(input('Enter divisor: '))
        result = arg1 / arg2
    except ZeroDivisionError:
        return 'Mo one can divide on null! '
    except ValueError:
        return 'Entered value is incorrect!'
    
    return result
print(f'Result is: {f_division()}')


