import csv
from matplotlib import pyplot as plt
from datetime import datetime

flag = int(input(':'))

if flag == 1:
    filename = 'sitka_weather_07-2014.csv'
elif flag == 2:
    filename = 'sitka_weather_2014.csv'
elif flag == 3:
    filename = 'death_valley_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    headers = next(reader)

    date = []
    maxt = []
    mint = []

    for index, head in enumerate(headers):
        print(index, head)

    for row in reader:
        try:
            h_t = int(row[1])
            m_t = int(int(row[3]))
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print('Данные не были записаны.')
        else:
            maxt.append(h_t)
            mint.append(m_t)
            date.append(current_date)

    print(maxt)
    print(date)

    fig = plt.figure(dpi=128, figsize=(20, 12))
    plt.plot(date, maxt, color='red')
    plt.plot(date, mint, color='blue')
    plt.fill_between(date,maxt,mint, facecolor = 'green', alpha = 0.2)
    plt.title('График температуры за 2014 год', fontsize=34)
    plt.xlabel('Дата', fontsize =28)
    plt.ylabel('Температура', fontsize=28)
    plt.tick_params(axis='both', which='major', labelsize=22)
    fig.autofmt_xdate()
    plt.show()