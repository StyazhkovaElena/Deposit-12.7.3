kol = int(input("Введите колличество билетов: \n"))
price = 0
for i in range(int(kol)):
    age = int( input("Укажите возраст:"))
    if age < 18 :
        price += 0
    elif 18 <= age < 25:
        price += 990
    else :
        price += 1390
if int(kol) < 3:
    print("Общая стоимость билетов:", int(price))
else:
    price = price - price * 10 / 100
    print("Стоимость с учетом скидки: ", int(price))
