# Paso 9: estructura real del Excel de CAC/BCR

Ya tenemos algo muy importante: la inspección real del archivo que descargaste.

## Estructura observada

La hoja se llama:

- `Worksheet`

Las primeras filas útiles aparecen así:

- fila 1: `Consulta de precios`
- fila 4: `Trigo`
- fila 5: encabezados reales

## Encabezados reales detectados

Los encabezados útiles del archivo son:

- `Fecha de operación`
- `Precio`

## Ejemplo real de datos

A partir de la fila 6 empiezan a aparecer registros como estos:

- `2026-03-05 03:00:00` → `253000`
- `2026-03-06 03:00:00` → `260000`
- `2026-03-09 03:00:00` → `257500`

## Qué significa esto para el proyecto

Esto es excelente, porque ahora ya sabemos que el normalizador tiene que soportar explícitamente:

1. el encabezado `Fecha de operación`,
2. el encabezado `Precio`,
3. fechas con formato `YYYY-MM-DD HH:MM:SS`.

## Próximo paso técnico

Con esta información, el siguiente paso es usar el normalizador actualizado para convertir el Excel real a CSV estándar.
