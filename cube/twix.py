import pygal
from cube import Cube

n1 = int(input('Введите количество граней первого кубика'))
n2 = int(input('Введите количество граней второго кубика'))

cube_1 = Cube(n1)
cube_2 = Cube(n2)

overall_v = []
v1 = []
v2 = []

for i in range (0,1000):
    first = cube_1.roll()
    second = cube_2.roll()

    v1.append(first)
    v2.append(second)
    overall_v.append(first+second)


r1 = [v1.count(value) for value in range(1, cube_1.sides+1)]
r2 = [v2.count(value) for value in range(1, cube_2.sides+1)]
overall_r = [overall_v.count(value) for value in range(2, cube_1.sides+cube_2.sides+1)]

xaxs = []
for k in range (2,cube_1.sides+cube_2.sides+1):
    xaxs.append(str(k))

hist = pygal.Bar()
hist.title = 'Результаты совместных бросков 2-ух кубиков'
hist.x_labels = xaxs
hist.x_title = 'Выпавшие числа'
hist.y_title = 'Количество выпадений'
hist.add('D'+str(n1)+' + '+'D'+str(n2), overall_r)
hist.render_to_file('two.svg')
hist.add('First D'+str(n1), r1)
hist.add('Second D'+str(n2), r2)
hist.render_to_file('advanced_two.svg')
