"""
Case-study #2
Developers:
Marinkin O. (33,33333333333333%),
Seledtsov A. (33,33333333333333%),
Evdischenko M. (53,33333333333333%).
"""

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

"""
constants for the stage of the tax
first (constant stage) = 0, sixth (constant stage) = 405100
second, third, fourth, fifth, seventh are variable
"""

if subject_of_taxation == 'одинсубъект':
    sec = 9075
    thi = 36900
    fou = 89350
    fif = 186350
    sev = 406750
elif subject_of_taxation == 'супружескаяпара':
    sec = 18150
    thi = 73800
    fou = 148850
    fif = 226850
    sev = 457600
elif subject_of_taxation == 'родитель-одиночка' or subject_of_taxation == 'родительодиночка':
    sec = 12950
    thi = 49400
    fou = 127550
    fif = 206600
    sev = 432200

# calculating the tax amount
if 0 <= annual_income <= sec:
    tax = 0.10 * annual_income
    print('Сумма годового налога составит: ', tax)
elif sec < annual_income <= thi:
    tax = 0.10 * sec + 0.15 * (annual_income - sec)
    print('Сумма годового налога составит: ', tax)
elif thi < annual_income <= fou:
    tax = 0.10 * sec + 0.15 * (thi - sec) + 0.25 * (annual_income - thi)
    print('Сумма годового налога составит: ', tax)
elif fou < annual_income <= fif:
    tax = 0.10 * sec + 0.15 * (thi - sec) + 0.25 * (fou - thi) + 0.28 * (annual_income - fou)
    print('Сумма годового налога составит: ', tax)
elif fif < annual_income <= 405100:
    tax = 0.10 * sec + 0.15 * (thi - sec) + 0.25 * (fou - thi) + 0.28 * (fif - fou) + 0.33 * \
          (annual_income - fif)
    print('Сумма годового налога составит: ', tax)
elif 405100 < annual_income <= sev:
    tax = 0.10 * sec + 0.15 * (thi - sec) + 0.25 * (fou - thi) + 0.28 * (fif - fou) + 0.33 * \
          (405100 - fif) + 0.35 * (annual_income - 405100)
    print('Сумма годового налога составит: ', tax)
elif sev < annual_income:
    tax = 0.10 * sec + 0.15 * (thi - sec) + 0.25 * (fou - thi) + 0.28 * (fif - fou) + 0.33 * \
          (405100 - fif) + 0.35 * (sev - 405100) + 0.396 * (annual_income - sev)
    print('Сумма годового налога составит: ', tax)
