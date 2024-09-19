from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().split('\n')

reader = csv.reader(lines)
header_row = next(reader)
#extract dates, high and low temperatures from the file
highs, lows, dates = [], [], []
for row in reader:
    if len(row) >= 5:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)

#plot highs and lows temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

#format plot
plt.title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
"""print(highs)

#find the index of the header row
for index, column_header in enumerate(header_row):
    print(index, column_header)"""


