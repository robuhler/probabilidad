# Paso 8: mapa simple de carpetas y scripts

Esta guía es para que sepas **dónde está cada cosa** dentro del proyecto.

## Carpeta principal del proyecto

La carpeta principal sobre la que estamos trabajando se llama:

- `trigo_prediccion/`

## Qué hay adentro de `trigo_prediccion/`

### 1. `docs/`
Acá están los textos explicativos.

Ejemplo:
- `trigo_prediccion/docs/paso_03_fuente_precio_spot.md`

### 2. `spot_trigo/`
Acá están los archivos que hacen el trabajo práctico sobre el precio spot del trigo.

## Qué hay adentro de `trigo_prediccion/spot_trigo/`

### Scripts
Los scripts son los archivos `.py` que se ejecutan.

Los principales son:

- `trigo_prediccion/spot_trigo/inspect_cac_excel.py`
- `trigo_prediccion/spot_trigo/normalize_cac_excel.py`
- `trigo_prediccion/spot_trigo/update_master.py`
- `trigo_prediccion/spot_trigo/generate_report.py`
- `trigo_prediccion/spot_trigo/run_pipeline.py`

### Carpetas de trabajo

- `trigo_prediccion/spot_trigo/inbox_excel/` → acá guardás el Excel descargado desde la web.
- `trigo_prediccion/spot_trigo/normalized/` → acá queda el CSV ya normalizado.
- `trigo_prediccion/spot_trigo/master/` → acá queda la base histórica consolidada.
- `trigo_prediccion/spot_trigo/reports/` → acá queda el informe final.
- `trigo_prediccion/spot_trigo/samples/` → acá hay un archivo de ejemplo para probar.

## Cómo verlo en PyCharm

Si abrís el proyecto en PyCharm, deberías ver algo parecido a esto:

```text
trigo_prediccion/
├── docs/
└── spot_trigo/
    ├── inspect_cac_excel.py
    ├── normalize_cac_excel.py
    ├── update_master.py
    ├── generate_report.py
    ├── run_pipeline.py
    ├── inbox_excel/
    ├── normalized/
    ├── master/
    ├── reports/
    └── samples/
```

## Qué hace cada script, explicado simple

### `inspect_cac_excel.py`
Sirve para mirar cómo viene armado el Excel real.

### `normalize_cac_excel.py`
Sirve para transformar el Excel a un CSV estándar que nuestro proyecto pueda leer.

### `update_master.py`
Sirve para sumar los nuevos datos a la base histórica.

### `generate_report.py`
Sirve para armar el informe con tabla y gráfico.

### `run_pipeline.py`
Sirve para ejecutar el flujo completo de una forma más cómoda, ya sea arrancando desde un Excel o desde un CSV normalizado.
