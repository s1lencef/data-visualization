from random import randint
from matplotlib import pyplot as plt


class Cube:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

my_cube = Cube()

points=[]
y_values =[]

for k in range(0,1000):
    points.append(my_cube.roll())

x_values = [k for k in range(1,my_cube.num_sides)]
for x in x_values:
    y_values.append(points.count(x))
print(points)
print(x_values)
print(y_values)

plt.bar(x_values,y_values,color = 'red', edgecolor = 'green', linewidth = 2)
plt.title('Кубик 6 граней', fontsize = 24)
plt.ylabel('Количество выпадений каждого числа', fontsize = 16)
plt.xlabel('Возможные числа', fontsize = 16)
plt.tick_params( axis = 'both', labelsize = 12)
plt.show()