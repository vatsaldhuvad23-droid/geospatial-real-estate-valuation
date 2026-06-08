import pandas as pd
import folium

df = pd.read_csv("data/outlier_removed.csv")

m = folium.Map(
    location=[df["lat"].mean(), df["long"].mean()],
    zoom_start=10
)

for i in range(min(100, len(df))):
    folium.Marker(
        [df.iloc[i]["lat"], df.iloc[i]["long"]]
    ).add_to(m)

m.save("reports/housing_map.html")

print("Map saved successfully.")