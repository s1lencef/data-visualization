import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as file:
    reader = csv.reader(file)
    headers = next(reader)
    for index, column in enumerate(headers):
        print(index, column)
    highs = []
    data = []

    for row in reader:
        highs.append(int(row[1]))
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        data.append(current_date)


    print(data)
    print(highs)

    fig = plt.figure(dpi=128, figsize = (10,6))
    plt.plot(data, highs, color = 'green' )
    plt.title('Максимальные значения температуры \n в каком-то американском Устьурюпинске в июле', fontsize = 16)
    plt.xlabel('Дата', fontsize = 16)
    plt.ylabel('Максимальная температура в фарингейтах', fontsize =14)
    plt.tick_params(axis ='both', which = 'major', labelsize = 14)
    fig.autofmt_xdate()

    plt.show()
    print(data[0])