import plotly.express as px
from die import Die
#create two Dice.
die_1 = Die()
die_2 = Die()

#make some rolls and store results in a list.
results = []
for roll_numn in range(1000):
    result =die_1.roll() + die_2.roll()
    results.append(result)

#analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
title = "Results of rolling two Dice 1000 times."
labels = {'x':'Result', 'y':'Frequency of Result'} #defining axix labels as dictionary
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()