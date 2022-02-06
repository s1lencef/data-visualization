from random import choice

class Randomwalk():
    def __init__(self,count_points=5000):
        self.count_points = count_points
        self.x_values = [0]
        self.y_values = [0]

    def step(self):
        """вычисляет насколько точка сдвинется от предыдущего положения"""
        direction = choice([1,-1])
        length = choice(range(0,8))
        result = direction*length
        return result

    def walk(self):
        """заполняет массивы данных с координатами точки по х и у в каждый момент времени"""
        while len(self.x_values) < self.count_points:
            #Вычисление сдвигов по каждой оси каждый шаг
            x_step = self.step()
            y_step = self.step()

            #Игнорируем нулевые значения(так как в моделируемой ситуации точка на месте не стоит)
            if x_step == y_step == 0:
                continue
            #Вычисление новых координат после сдвига
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1] + y_step
            #Добавляем новую координату в массив
            self.x_values.append(next_x)
            self.y_values.append(next_y)
