from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().split('\n')

reader = csv.reader(lines)
header_row = next(reader)
#extract high temperatures from the file
highs = []
for row in reader:
    if len(row) >= 5:
        high = int(row[4])
        highs.append(high)

#plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

#format plot
plt.title("Daily high temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
"""print(highs)

#find the index of the header row
for index, column_header in enumerate(header_row):
    print(index, column_header)"""


