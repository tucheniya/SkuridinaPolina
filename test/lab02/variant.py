total_volume = int(input("Количество деталей: "))
capacity = int(input("Количество деталей в одном контейнере: "))

full_units = total_volume // capacity
remainder = total_volume % capacity
units_needed = (total_volume + capacity - 1) // capacity

print(f"Количество контейнеров: {full_units}")
print(f"Остаток: {remainder}")
print(f"Всего деталей нужно: {units_needed}")
