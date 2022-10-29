per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = []

for i in per_cent:
    deposit.append(int(money/100*per_cent[i]))
maximal = max(deposit)

print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", maximal)
