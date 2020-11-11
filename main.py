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
print('Ваш сумарный доход:', annual_income)

# main questions
tax_deduction = float(input('Сумма налогового вычета: '))
subject_of_taxation = input('Субъект налогообложения: ').lower().replace(' ', '')
if not('одинсубъект' or 'супружескаяпара' or 'родитель-одиночка' or 'родительодиночка'):
    print('Некорректный ввод субъекта налогообложения.')

# income without tax deduction
annual_income = annual_income - tax_deduction

# constants for the stage of the tax
if subject_of_taxation == 'одинсубъект':
    second = 9075
    third = 36900
    fourth = 89350
    fifth = 186350
    seventh = 406750
elif subject_of_taxation == 'супружескаяпара':
    second = 18150
    third = 73800
    fourth = 148850
    fifth = 226850
    seventh = 457600
elif subject_of_taxation == 'родитель-одиночка' or subject_of_taxation == 'родительодиночка':
    second = 12950
    third = 49400
    fourth = 127550
    fifth = 206600
    seventh = 432200

# main
if 0 <= annual_income <= second:
    tax = 0.10 * annual_income
    print('Сумма годового налога составит: ', tax)
elif second < annual_income <= third:
    tax = 0.10 * second + 0.15 * (annual_income - second)
    print('Сумма годового налога составит: ', tax)
elif third < annual_income <= fourth:
    tax = 0.10 * second + 0.15 * (third - second) + 0.25 * (annual_income - third)
    print('Сумма годового налога составит: ', tax)
elif fourth < annual_income <= fifth:
    tax = 0.10 * second + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (annual_income - fourth)
    print('Сумма годового налога составит: ', tax)
elif fifth < annual_income <= 405100:
    tax = 0.10 * second + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
            annual_income - fifth)
    print('Сумма годового налога составит: ', tax)
elif 405101 < annual_income <= seventh:
    tax = 0.10 * second + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
                    405101 - fifth) + 0.35 * (annual_income - 405101)
    print('Сумма годового налога составит: ', tax)
elif seventh < annual_income:
    tax = 0.10 * second + 0.15 * (third - second) + 0.25 * (fourth - third) + 0.28 * (fifth - fourth) + 0.33 * (
                    405101 - fifth) + 0.35 * (seventh - 405101) + 0.396 * (annual_income - seventh)
    print('Сумма годового налога составит: ', tax)
