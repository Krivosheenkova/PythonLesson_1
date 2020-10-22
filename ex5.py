# Ex. 5
revenue = float(input("Enter the company's revenue amount, $: "))
expences = float(input("Enter the company's expences amount, $: "))
profit = revenue - expences
if revenue > expences:
    print('The result is PROFIT, but do not relax!')
    profitability = (profit / revenue) * 0.1
    print('Profitability of your company:', "%.2f" % (profitability), '%')
    staff = int(input('Enter number of employees: '))
    salary = profit / staff
    print('The salary per employee: ', salary, '$')
elif revenue == expences:
    print('You went to ZERO, that is not pretty good, but ok')
else:
    print('The result is LOSS, you need to change something!')
