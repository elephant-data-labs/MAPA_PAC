# Elephant Data Labs — Mapa de Pedro Aguirre Cerda

Aplicación geoespacial construida con Python, GeoPandas, Folium y Streamlit.

## Estructura

```text
.
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   ├── pedro_aguirre_cerda.geojson
│   └── sample_points.csv
├── scripts/
│   └── prepare_geojson.py
└── assets/
```

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicar en GitHub

1. Crea un repositorio nuevo en GitHub.
2. Sube todos los archivos de esta carpeta.
3. En Streamlit Community Cloud selecciona el repositorio.
4. Usa `app.py` como archivo principal.

## Nota sobre los datos

El archivo `data/pedro_aguirre_cerda.geojson` corresponde a la geometría generada desde el shapefile entregado para este proyecto. Antes de usarlo con fines oficiales, regulatorios o cartográficos, valida su fuente, escala, sistema de referencia y licencia.
