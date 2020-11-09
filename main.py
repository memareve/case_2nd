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
    if 0 <= annual_income <= 18150:

    elif 18151 <= annual_income <= 73800:

    elif 73801 <= annual_income <= 148850:

    elif 148851 <= annual_income <= 226850:

    elif 226851 <= annual_income <= 405100:

    elif 405101 <= annual_income <= 457600:

    elif annual_income >= 457601:


elif subject_of_taxation == 'родитель-одиночка':
    if 0 <= annual_income <= 12950:

    elif 12951 <= annual_income <= 49400:

    elif 49401 <= annual_income <= 127550:

    elif 127551 <= annual_income <= 206600:

    elif 206601 <= annual_income <= 405100:

    elif 405101 <= annual_income <= 432200:

    elif annual_income >= 432201:


