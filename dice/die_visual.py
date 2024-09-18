import plotly.express as px
from die import Die
#create a D6.
die = Die()

#make some rolls and store results in a list.
results = []
for roll_numn in range(1000):
    result =die.roll()
    results.append(result)

#analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
title = "Results of rolling one Dice 1000 times."
labels = {'x':'Result', 'y':'Frequency of Result'} #defining axix labels as dictionary
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()