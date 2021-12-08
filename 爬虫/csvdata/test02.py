import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, header in enumerate(header_row):
    #     print(index,header)
    highs = []
    date = []
    lows = []
    for row in reader:
        try:
            date1 = datetime.strptime(row[0], "%Y-%m-%d")
            highs.append(int(row[1]))
            lows.append(int(row[2]))
        except ValueError:
            print("error")
        else:
            date.append(date1)
    # print(highs)

plt.figure(dpi=300, figsize=(10, 6))
plt.plot(date, highs, c='red')
plt.plot(date, lows, c='blue')
plt.title("7月最高气温", fontsize=18)
plt.xlabel("日期", fontsize=14)
plt.ylabel("气温", fontsize=14)
plt.tick_params(axis='both', labelsize=10)
plt.fill_between(date, highs, lows, facecolor='orange', alpha=0.3)

plt.savefig("death_2014.png",bbox_inches='tight')
plt.show()
