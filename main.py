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
subject_of_taxation = input('Субъект налогообложения: ').lower().replace(' ', '')
tax_deduction = float(input('Сумма налогового вычета: '))

annual_income = annual_income - tax_deduction

if subject_of_taxation == 'одинсубъект':
    if 0 <= annual_income <= 9075:
        tax = 0.1 * (annual_income - 0)
        print('Сумма годового налога составит: ', tax)
    elif 9076 <= annual_income <= 36900:
        tax = 0.1 * (9076 - 0) + 0.15 * (annual_income - 9076)
        print('Сумма годового налога составит: ', tax)
    elif 36901 <= annual_income <= 89350:
        tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (annual_income - 36901)
        print('Сумма годового налога составит: ', tax)
    elif 89351 <= annual_income <= 186350:
        tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (annual_income - 89351)
        print('Сумма годового налога составит: ', tax)
    elif 186351 <= annual_income <= 405100:
        tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    annual_income - 186351)
        print('Сумма годового налога составит: ', tax)
    elif 405101 <= annual_income <= 406750:
        tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405101 - 186351) + 0.35 * (annual_income - 405101)
        print('Сумма годового налога составит: ', tax)
    elif annual_income >= 406751:
        tax = 0.1 * (9076 - 0) + 0.15 * (36901 - 9076) + 0.25 * (89351 - 36901) + 0.28 * (186351 - 89351) + 0.33 * (
                    405101 - 186351) + 0.35 * (406751 - 405101) + 0.396 * (annual_income - 406751)
        print('Сумма годового налога составит: ', tax)

elif subject_of_taxation == 'супружескаяпара':
    if 0 <= annual_income <= 18150:
        tax = 0.1 * (annual_income - 0)
        print('Сумма годового налога составит: ', tax)
    elif 18151 <= annual_income <= 73800:
        tax = 0.1 * (18151 - 0) + 0.15 * (annual_income - 18151)
        print('Сумма годового налога составит: ', tax)
    elif 73801 <= annual_income <= 148850:
        tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (annual_income - 73801)
        print('Сумма годового налога составит: ', tax)
    elif 148851 <= annual_income <= 226850:
        tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (annual_income - 148851)
        print('Сумма годового налога составит: ', tax)
    elif 226851 <= annual_income <= 405100:
        tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                annual_income - 226851)
        print('Сумма годового налога составит: ', tax)
    elif 405101 <= annual_income <= 457600:
        tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                405101 - 226851) + 0.35 * (annual_income - 405101)
        print('Сумма годового налога составит: ', tax)
    elif annual_income >= 457601:
        tax = 0.1 * (18151 - 0) + 0.15 * (73801 - 18151) + 0.25 * (148851 - 73801) + 0.28 * (226851 - 148851) + 0.33 * (
                405101 - 226851) + 0.35 * (457601 - 405101) + 0.396 * (annual_income - 457601)
        print('Сумма годового налога составит: ', tax)

elif subject_of_taxation == 'родитель-одиночка':
    if 0 <= annual_income <= 12950:

    elif 12951 <= annual_income <= 49400:

    elif 49401 <= annual_income <= 127550:

    elif 127551 <= annual_income <= 206600:

    elif 206601 <= annual_income <= 405100:

    elif 405101 <= annual_income <= 432200:

    elif annual_income >= 432201:



