# Case-study #2
# Developers: Marinkin O. (33,33333333333333%),
# Seledtsov A. (33,33333333333333%),
# Evdischenko M. (33,33333333333333%).

# calculating_annual_income
name_month = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре',
              'декабре']
QUESTION = 'Ваш доход в'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month]), end=' ')
    income = float(input())
    annual_income += income

# main questions
tax_deduction = float(input('Сумма налогового вычета: '))
subject_of_taxation = input('Субъект налогообложения: ').lower().replace(' ', '')
if not('одинсубъект' or 'супружескаяпара' or 'родитель-одиночка' or 'родительодиночка'):
    print('Некорректный ввод субъекта налогообложения.')

# income without tax deduction
annual_income = annual_income - tax_deduction

# constants for the stage of the tax
if subject_of_taxation == 'одинсубъект':
    second = 9076
    third = 36901
    fourth = 89351
    fifth = 186351
    seventh = 406751
elif subject_of_taxation == 'супружескаяпара':
    second = 18151
    third = 73801
    fourth = 148851
    fifth = 226851
    seventh = 457601
elif subject_of_taxation == 'родитель-одиночка' or subject_of_taxation == 'родительодиночка':
    second = 12951
    third = 49401
    fourth = 127551
    fifth = 206601
    seventh = 432201

# main
if 0 <= annual_income <= (second - 1):
    tax = 0.10 * (annual_income - 0)
    print('Сумма годового налога составит: ', tax)
elif second <= annual_income <= (third - 1):
    tax = 0.10 * (second - 0) + 0.15 * (annual_income - second)
    print('Сумма годового налога составит: ', tax)
elif third <= annual_income <= (fourth - 1):
    tax = 0.10 * (second - 0) + 0.15 * (third - second) + 0.25 * (annual_income - third)
    print('Сумма годового налога составит: ', tax)
elif fourth <= annual_income <= (fifth - 1):
    tax = 0.10 * (second - 0) + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (annual_income - fourth)
    print('Сумма годового налога составит: ', tax)
elif fifth <= annual_income <= 405100:
    tax = 0.10 * (second - 0) + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
            annual_income - fifth)
    print('Сумма годового налога составит: ', tax)
elif 405101 <= annual_income <= (seventh - 1):
    tax = 0.10 * (second - 0) + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
                    405101 - fifth) + 0.35 * (annual_income - 405101)
    print('Сумма годового налога составит: ', tax)
elif seventh <= annual_income:
    tax = 0.10 * (second - 0) + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
                    405101 - fifth) + 0.35 * (seventh - 405101) + 0.396 * (annual_income - seventh)
    print('Сумма годового налога составит: ', tax)
