from randomwalk import Randomwalk
import matplotlib.pyplot as plt
count = int(input('Введите количество шагов в блуждании: '))
while True:
    my_rw = Randomwalk(count)
    my_rw.walk()

    numbers = list(range(0,my_rw.count_points))

    plt.scatter(my_rw.x_values, my_rw.y_values, c=numbers, s=15, edgecolor = 'none', cmap = plt.cm.Greens)
    plt.scatter(my_rw.x_values[0], my_rw.y_values[0], c='blue')
    plt.scatter(my_rw.x_values[-1], my_rw.y_values[-1], c='red')
    plt.axis('off')
    plt.show()
    end = input("Создать еще одно блуждание? (да/нет)")
    if end=='нет':
        break




