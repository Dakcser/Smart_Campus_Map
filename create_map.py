import folium
from folium import plugins
from folium.plugins import HeatMap

m = folium.Map([65.06, 25.467], zoom_start=14.5)

folium.raster_layers.ImageOverlay(
    image="./university_map.png",
    name="university map",
    bounds=[[65.062044, 25.462502], [65.056337, 25.471510]],
    opacity=1,
    interactive=False,
    cross_origin=False,
    zindex=1).add_to(m)


data = [[65.05776, 25.46895, 0],
 [65.05715, 25.46785, 0],
 [65.06087, 25.46683, 1],
 [65.06107, 25.46675, 0],
 [65.05813404631877, 25.466177165508274, 0],
 [65.05849, 25.46598, 0],
 [65.05865, 25.4656, 0],
 [65.05785, 25.46718, 1],
 [65.05806, 25.46922, 0],
 [65.05882, 25.46564, 0],
 [65.06352, 25.4653, 0],
 [65.05916, 25.46565, 0],
 [65.05788437215459, 25.46949237585068, 0],
 [65.06146, 25.4672, 0],
 [65.06343, 25.46577, 14],
 [65.05891, 25.46798, 0],
 [65.05745, 25.46926, 0],
 [65.0611, 25.46679, 2],
 [65.05786, 25.46883, 0],
 [65.05864, 25.46656, 0],
 [65.05769, 25.4676, 0],
 [65.06043, 25.46667, 2],
 [65.05813404631877, 25.466177165508274, 0],
 [65.05973, 25.46816, 0],
 [65.06123, 25.46752, 0],
 [65.05862, 25.46645, 0],
 [65.05701, 25.46774, 0],
 [65.05804068316928, 25.466609521425063, 74],
 [65.05877, 25.46786, 1]
]


HeatMap(data).add_to(folium.FeatureGroup(name='Heat Map').add_to(m))

folium.LayerControl(render=True).add_to(m)

# Display the map
m.save(outfile="index.html")
