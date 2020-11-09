# Case-study #2
# Developers: Marinkin O. ( ),
# Seledtsov A. ( ),
# Evdischenko M. ( ).

# calculating_annual_income
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
QUESTION = 'Ваш доход в'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end=''))
    income = float(input())
    annual_income += income

# main questions
subject_of_taxation = input('Субъект налогообложения:').lower().replace(' ', '')
tax_deduction = input('Сумма налогового вычета: ')

annual_income = annual_income - tax_deduction

if subject_of_taxation == 'одинсубъект':
    if 0 <= annual_income <= 9075:

    elif 9076 <= annual_income <= 36900:

    elif 36901 <= annual_income <= 89350:

    elif 89351 <= annual_income <= 186350:

    elif 186351 <= annual_income <= 405100:

    elif 405101 <= annual_income <= 406750:

    elif annual_income >= 406751:


elif subject_of_taxation == 'супружескаяпара':


elif subject_of_taxation == 'родитель-одиночка':



