money = float(input ("Введите сумму, которую хотите вложить:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int(money*per_cent['ТКБ']/100)
SKB = int(money*per_cent['СКБ']/100)
VTB = int(money*per_cent['ВТБ']/100)
SBER = int(money*per_cent['СБЕР']/100)
deposit = [ TKB,  SKB,  VTB,  SBER]
print(deposit)
print("Максимальная прибыль будет:", max(deposit))