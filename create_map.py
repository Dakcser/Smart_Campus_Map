import folium

m = folium.Map([65.06, 25.467], zoom_start=14.5)

m.save(outfile="Smart_campus_map.html")

# Display the map
m 
