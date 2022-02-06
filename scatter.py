import matplotlib.pyplot as plt
while(True):
    n = int(input("Введите количество значений"))
    args = [i for i in range(0,n+1)]

    deg = int(input("Какой степени построить график?(1,2,3,4)"))
    values = [args[i]**deg for i in range(0,n+1)]
    values_2 = [args[i] ** (deg-1) for i in range(0, n + 1)]

    plt.scatter(args, values,c=values, s=50, edgecolor ='none', cmap = plt.cm.Blues)
    plt.title("Говно", fontsize=21)
    plt.xlabel("Залупа", fontsize=15)
    plt.ylabel("Пенис", fontsize=15)
    plt.tick_params(axis='both',labelsize=11)

    plt.savefig('xuz.png', bbox_inches='tight')
    plt.show()
    plt.scatter(args, values_2, c=values_2, s=50, edgecolor='none', cmap=plt.cm.Greens)
    plt.savefig('xuz2.png', bbox_inches='tight')
    plt.show()
    if deg == 2:
        deg_name = "квадрате"
    elif deg ==3:
        deg_name = "кубе"
    else:
        deg_name = str(deg)+"-ой степени"

    flag = input('Продолжить? ')
    if flag == 'нет':
        break
