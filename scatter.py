import matplotlib.pyplot as plt
def found_y_name(deg):
    if deg == 2:
        y_name = "квадрате"
    elif deg ==3:
        y_name = "кубе"
    else:
        y_name = str(deg)+"-ой степени"
    return y_name
while(True):
    n = int(input("Введите количество значений"))
    args = [i for i in range(0,n+1)]

    deg = int(input("Какой степени построить график?(1,2,3,4)"))
    values = [args[i]**deg for i in range(0,n+1)]
    deg_name = found_y_name(deg)

    plt.scatter(args, values,c=values, s=50, edgecolor ='none', cmap = plt.cm.Blues)
    plt.title("Точки", fontsize=21)
    plt.xlabel("Параметр", fontsize=15)
    plt.ylabel("Значение в " + deg_name, fontsize=15)
    plt.tick_params(axis='both',labelsize=11)

    plt.savefig('xuz.png', bbox_inches='tight')
    plt.show()

    if deg>1:
        deg-=1
        values_2 = [args[i]**(deg) for i in range(0, n + 1)]
        deg_name = found_y_name(deg)

        plt.scatter(args, values_2, c=values_2, s=50, edgecolor='none', cmap=plt.cm.Greens)
        plt.title("Точки", fontsize=21)
        plt.xlabel("Параметр", fontsize=15)
        plt.ylabel("Значение в " + deg_name, fontsize=15)
        plt.tick_params(axis='both', labelsize=11)

        plt.savefig('xuz2.png', bbox_inches='tight')
        plt.show()

    flag = input('Продолжить? ')
    if flag == 'нет':
        break