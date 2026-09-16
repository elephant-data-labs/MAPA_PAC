import json
from pathlib import Path

import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Elephant Data Labs | Pedro Aguirre Cerda",
    page_icon="🐘",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
GEOJSON_PATH = BASE_DIR / "data" / "pedro_aguirre_cerda.geojson"
POINTS_PATH = BASE_DIR / "data" / "sample_points.csv"

st.title("🐘 Elephant Data Labs")
st.subheader("Mapa geoespacial de Pedro Aguirre Cerda")

st.info(
    "Proyecto demostrativo de análisis geoespacial con datos públicos. "
    "La geometría comunal se carga desde un archivo GeoJSON."
)

with GEOJSON_PATH.open("r", encoding="utf-8") as f:
    comuna_geojson = json.load(f)

points = pd.read_csv(POINTS_PATH)

m = folium.Map(
    location=[-33.493, -70.678],
    zoom_start=13,
    tiles="CartoDB positron",
)

folium.GeoJson(
    comuna_geojson,
    name="Pedro Aguirre Cerda",
    style_function=lambda feature: {
        "fillColor": "#2563eb",
        "color": "#1e3a8a",
        "weight": 2,
        "fillOpacity": 0.25,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["comuna", "codigo_comuna"],
        aliases=["Comuna", "Código comunal"],
        localize=True,
    ),
).add_to(m)

for _, point in points.iterrows():
    folium.Marker(
        location=[point["lat"], point["lon"]],
        popup=f'{point["name"]}<br>Categoría: {point["category"]}',
        tooltip=point["name"],
    ).add_to(m)

folium.LayerControl().add_to(m)

st_folium(m, width=None, height=650)

st.caption(
    "Elephant Data Labs — análisis reproducible de datos públicos. "
    "Revisa la fuente y licencia del GeoJSON antes de publicar."
)
