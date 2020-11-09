# Case-study #2
# Developers: Marinkin O. ( ),
# Seledtsov A. ( ),
# Evdischenko M. ( ).

# calculating_annual_income
# string constants
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
QUESTION = 'Ваш доход в'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end=''))
    income = float(input())
    annual_income += income
print(annual_income)
