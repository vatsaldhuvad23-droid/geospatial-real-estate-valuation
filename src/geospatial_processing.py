import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load processed dataset
df = pd.read_csv("data/outlier_removed.csv")

# Create geometry column
geometry = [
    Point(xy)
    for xy in zip(df["long"], df["lat"])
]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=geometry
)

print(gdf.head())

# Save as GeoJSON
gdf.to_file(
    "reports/houses.geojson",
    driver="GeoJSON"
)

print("GeoJSON file saved successfully.")