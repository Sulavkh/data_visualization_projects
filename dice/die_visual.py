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
fig = px.bar(x=poss_results, y=frequencies)
fig.show()