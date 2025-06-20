import cartopy.crs as ct
import matplotlib.pyplot as plt
import cartopy.feature as cs
import streamlit as st
import io
st.title("Flight Path App")
fig = plt.figure(figsize=(11, 11))
m = fig.add_subplot(1, 1, 1, projection=ct.PlateCarree())
m.set_extent([-180, 180, -90, 90], crs=ct.PlateCarree())
m.add_feature(cs.OCEAN)
m.add_feature(cs.LAND)
m.add_feature(cs.COASTLINE)
m.add_feature(cs.STATES)
m.add_feature(cs.BORDERS, edgecolor="green", linestyle="dotted")
m.add_feature(cs.RIVERS, color="blue")
m.add_feature(cs.LAKES, color="lightskyblue")
plt.title("Map of the world with major cities")
cities = {
    "London": (0.1, 51.5),
    "New York": (-74, 40.7),
    "Shanghai": (121.4, 31.2),
    "New Delhi": (77.2, 28.6),
    "Toronto": (-79.3, 43.6),
    "Moscow": (37.6, 55.7),
    "Rio de Janeiro": (-43.2, -22.9)

}
a = st.text_input("Enter a city name: ")
b = st.text_input("Enter another city name: ")

for keys, (lon, lat) in cities.items():
    m.plot(lon, lat, marker="o", color="Red", transform=ct.PlateCarree())
    m.text(lon + 2, lat, keys, color="Black", transform=ct.PlateCarree())
if st.button('map'):
    lon_Sha, lat_Sha = cities[a]
    lon_Tor, lat_Tor = cities[b]
    m.annotate('',xy=(lon_Tor,lat_Tor),xytext=(lon_Sha,lat_Sha),arrowprops={'arrowstyle':'->','color':'purple','linewidth':4},transform=ct.Geodetic())

    # m.plot([lon_Sha, lon_Tor],[lat_Sha, lat_Tor], color = "Black", linewidth = 4, transform = ct.Geodetic())
    plt.title(f"Flight path between {a} and {b}")
    st.pyplot(fig)
    img = io.BytesIO()
    plt.savefig(img, format='jpg')
    st.download_button("Download the Map Pic", img, file_name=f"Flight Path between {a} and {b}.jpg")
