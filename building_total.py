# "Различие атрибутов класса и экземпляра."
# 1) Создайте новый класс Buiding с атрибутом total
# 2) Создайте инициализатор для класса Buiding,
# который будет увеличивать атрибут количества созданных объектов класса Building total
# 3) В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# 4) Полученный код напишите в ответ к домашнему заданию

class Building:
    total = 0  # атрибут(объект)

    def __init__(self):
        Building.total += 1


for _ in range(40):
    Building()

print(Building.total)


