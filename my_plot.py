import matplotlib.pyplot as plt
while(True):
    n = int(input("Введите количество значений"))
    args = [i for i in range(0,n+1)]
    deg = int(input("Какой степени построить график?(1,2,3,4)"))
    values = [args[i]**deg for i in range(0,n+1)]
    plt.plot(args,values, linewidth = 5)
    plt.title("График примера прямой зависимости", fontsize = 21)
    plt.xlabel('Параметр', fontsize = 17)
    if deg == 2:
        deg_name = "квадрате"
    elif deg ==3:
        deg_name = "кубе"
    else:
        deg_name = str(deg)+"-ой степени"

    plt.ylabel('Значение в ' + deg_name, fontsize = 17)
    plt.show()
    flag = input('Продолжить? ')
    if flag == 'нет':
        break
    plt.show()
