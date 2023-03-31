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

m.save(outfile="index.html")

HeatMap([[65.062044, 25.462502, 1]]).add_to(folium.FeatureGroup(name='Heat Map').add_to(m))

folium.LayerControl().add_to(m)

# Display the map
m 
