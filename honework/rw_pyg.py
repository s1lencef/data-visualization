from randomwalk import Randomwalk
import pygal

rw = Randomwalk()
rw.walk()

values = []
test = [0, 0]

for k in range(0, rw.count_points):
    test[0] = rw.x_values[k]
    test[1] = rw.y_values[k]
    test = tuple(test)
    values.append(test)
    test = list(test)

print(values)
rw_line = pygal.XY(stroke = False)
rw_line.title = 'Реализация случайного блуждания на PyGal'
rw_line.add('randomwalk', values)
rw_line.render_to_file('ff.svg')
