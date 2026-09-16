from pathlib import Path
import geopandas as gpd

INPUT = Path("data/original.shp")
OUTPUT = Path("data/pedro_aguirre_cerda.geojson")

gdf = gpd.read_file(INPUT)

if gdf.crs is not None:
    gdf = gdf.to_crs(epsg=4326)

gdf.to_file(OUTPUT, driver="GeoJSON")
print(f"GeoJSON generado en: {OUTPUT}")
