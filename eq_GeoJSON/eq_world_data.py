from pathlib import Path
import json
import plotly.express as px

# read data as a string and conver tot Python object
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents =  path.read_text()
all_eq_data = json.loads(contents)

#examine all earthquake in dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles =[], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, 
    color_continuous_scale='blackbody_r', labels={'color':'Magnitude'}, projection='natural earth',
    hover_name=eq_titles,
    )
fig.show()

"""
#create more readable data
path =Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
"""