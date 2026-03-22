# Flujo operativo del precio spot del trigo

Este directorio contiene el flujo operativo inicial del proyecto para trabajar con una sola variable:

- **precio spot del trigo**.

La idea es que puedas avanzar en PyCharm paso a paso, con instrucciones simples y reproducibles.

## Objetivo de esta carpeta

Acá dejamos resuelto un proceso básico pero útil:

1. inspeccionar el Excel real descargado desde CAC/BCR,
2. normalizarlo a un CSV estándar,
3. actualizar una base maestra sin duplicados por fecha,
4. generar un reporte HTML sencillo,
5. correr todo el flujo desde un solo comando cuando te resulte más cómodo.

## Estructura de trabajo

- `inbox_excel/`: guardá acá el Excel descargado manualmente desde CAC/BCR.
- `inbox/`: espacio opcional para futuros CSV externos si alguna vez hiciera falta.
- `normalized/`: acá se genera el CSV normalizado.
- `master/`: acá queda la base histórica consolidada.
- `reports/`: acá se guarda el reporte HTML.
- `samples/`: ejemplos para probar el flujo.

## Qué hace cada script

### `inspect_cac_excel.py`
Muestra las primeras filas no vacías de cada hoja del Excel para entender su estructura antes de transformar nada.

### `normalize_cac_excel.py`
Lee el Excel, detecta las columnas de fecha y precio, y genera un CSV estándar.

### `update_master.py`
Toma un CSV normalizado y lo incorpora a la base maestra, dejando una sola fila por fecha.

### `generate_report.py`
Lee la base maestra y genera un reporte HTML con métricas simples, tabla y gráfico SVG.

### `run_pipeline.py`
Ejecuta el flujo completo.

- Si le pasás un **Excel**, primero lo normaliza y después actualiza la base + genera el reporte.
- Si le pasás un **CSV normalizado**, usa ese archivo directamente y saltea la normalización.

## Instalación de dependencias

```bash
pip install -r trigo_prediccion/requirements.txt
```

## Esquema del CSV normalizado

El CSV intermedio usa estas columnas:

- `date`
- `price_ars_tn`
- `source`
- `price_kind`
- `product`

## Comandos recomendados

### 1. Inspeccionar el Excel

**Con selector de archivos**

```bash
python trigo_prediccion/spot_trigo/inspect_cac_excel.py
```

**Indicando la ruta manualmente**

```bash
python trigo_prediccion/spot_trigo/inspect_cac_excel.py --input trigo_prediccion/spot_trigo/inbox_excel/archivo_descargado.xlsx
```

### 2. Normalizar el Excel a CSV

**Con selector de archivos**

```bash
python trigo_prediccion/spot_trigo/normalize_cac_excel.py
```

**Indicando entrada y salida**

```bash
python trigo_prediccion/spot_trigo/normalize_cac_excel.py --input trigo_prediccion/spot_trigo/inbox_excel/archivo_descargado.xlsx --output trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv
```

### 3. Actualizar la base maestra

```bash
python trigo_prediccion/spot_trigo/update_master.py --input trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv --master trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv
```

### 4. Generar el reporte HTML

```bash
python trigo_prediccion/spot_trigo/generate_report.py --master trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv --output trigo_prediccion/spot_trigo/reports/precio_spot_trigo_report.html
```

### 5. Ejecutar todo el flujo desde un Excel

```bash
python trigo_prediccion/spot_trigo/run_pipeline.py --input trigo_prediccion/spot_trigo/inbox_excel/archivo_descargado.xlsx
```

Ese comando normaliza el Excel, actualiza la base maestra y genera el reporte.

### 6. Ejecutar todo el flujo desde un CSV ya normalizado

```bash
python trigo_prediccion/spot_trigo/run_pipeline.py --input trigo_prediccion/spot_trigo/samples/precio_spot_trigo_ejemplo.csv
```

Ese comando omite la normalización y usa directamente el CSV indicado.

## Nota práctica

Si el Excel real cambia de formato y el normalizador no logra detectar las columnas, primero corré `inspect_cac_excel.py` para ver los encabezados exactos.

Con esa información podés ajustar rápido los alias de fecha y precio en `normalize_cac_excel.py`.
