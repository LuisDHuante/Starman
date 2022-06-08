import folium
import numpy as np

acolors=['red', 'blue', 'green', 'purple', 'orange', 'darkred',
'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
def make_image(flights,flares):
    m=folium.Map(tiles="Stamen Toner",center=[20,0],zoom_start=3,min_zoom=3)
    colors={}
    
    mt=0
    for f in flights:
        mt=max(mt,f[3])
    for f in flights:
        icao24,callsign,origin_country,time_position,longitude,latitude,velocity,true_track=f
        if(mt-time_position>20 ):
            continue
        if origin_country not in colors.keys():
            colors[origin_country]=acolors[np.random.randint(0,len(acolors))]
        folium.Marker(
        [latitude,longitude],
        popup=f"<b>{origin_country}</b> <i>{callsign.strip()}</i>: ({longitude},{latitude})",
        opacity=1,
        icon=folium.Icon(
            color=colors[origin_country],
            icon_color=colors[origin_country]
        )
        #tooltip=f"<i>{callsign}</i>",
        ).add_to(m)
    for f in flares:
        timestamp,latitude,longitude,classf,magn,radius=f
        folium.Circle(
            location=[latitude,longitude],
            radius=radius,
            popup=f"{classf}.{magn}",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
        ).add_to(m)
        
    m.save("/data/team1/map.html")
    return 0
