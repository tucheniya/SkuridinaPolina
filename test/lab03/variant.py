charge = int(input("Результат теста: "))

if charge < 0 or charge > 100:
    print("Ошибка диапазона")
elif charge <= 49:
    print("Нужна доработка")
elif charge <= 84:
    print("Зачёт")
else:
    print("Отличный результат")
