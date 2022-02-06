from cube import Cube
import pygal
c = Cube(10)
results = [c.roll() for i in range(0, 10000)]
count =[]

for value in range(1, c.sides+1):
    count.append(results.count(value))

column = pygal.Bar()
column.title = 'Броски кубика'
column.x_label = ['1','2','3','4','5','6']
column.x_title = 'Выпавшие числа'
column.y_title = 'Количество выпадений'
column.add('D6', count)
column.render_to_file('cube_histogramm.svg')
