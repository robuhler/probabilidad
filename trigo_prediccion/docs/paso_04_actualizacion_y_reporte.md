# Paso 4: actualización y reporte del precio spot

Una vez definida la fuente, el siguiente paso es dejar resuelto el flujo operativo de esta variable.

## Objetivo del flujo

Queremos poder hacer siempre estas tres cosas:

1. actualizar la serie histórica,
2. evitar duplicados,
3. ver rápidamente un informe ejecutivo.

## Estructura propuesta

El flujo del precio spot quedó organizado así:

- `trigo_prediccion/spot_trigo/inbox_excel/`: Excel descargados manualmente desde CAC/BCR.
- `trigo_prediccion/spot_trigo/normalized/`: CSV intermedios ya normalizados.
- `trigo_prediccion/spot_trigo/master/`: serie histórica consolidada.
- `trigo_prediccion/spot_trigo/reports/`: reporte ejecutivo automático.

## Qué resuelve este primer flujo

En esta primera versión dejamos automatizado:

- la inspección del Excel real antes de tocar el resto del proceso,
- la normalización del Excel a CSV estándar,
- la actualización de la base maestra,
- la generación de un reporte HTML con métricas, tabla y gráfico.

## Cómo se ejecuta el flujo completo

El script `trigo_prediccion/spot_trigo/run_pipeline.py` puede trabajar de dos maneras:

1. arrancando desde un **Excel** descargado,
2. arrancando desde un **CSV normalizado**.

Eso permite usar el mismo flujo tanto para el caso real como para pruebas rápidas con archivos de ejemplo.

## Qué dejamos para el siguiente subpaso técnico

Todavía puede quedar pendiente automatizar la extracción directa desde la web si la fuente requiere una interacción especial.

Pero aunque eso pase, ya dejamos preparado el corazón del proceso: normalización + base maestra + reporte.
