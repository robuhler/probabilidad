# Paso 10: normalizar el Excel real

Excelente: la inspección del Excel ya funcionó bien.

Eso significa que ya podemos pasar al siguiente paso práctico.

## Objetivo de este paso

Convertir el Excel descargado desde CAC/BCR en un CSV estándar que nuestro proyecto pueda usar.

## Archivo que tenés que ejecutar

El script que hace esto es:

- `trigo_prediccion/spot_trigo/normalize_cac_excel.py`

## Forma más simple de usarlo en PyCharm

Ahora el script puede ejecutarse sin argumentos.

Si lo corrés así:

```bash
python trigo_prediccion/spot_trigo/normalize_cac_excel.py
```

te va a abrir un selector de archivos para que elijas el Excel.

## Resultado esperado

Si todo sale bien, el script tiene que generar un archivo CSV normalizado en:

- `trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv`

## Qué quiero que me mandes después

Quiero que me pegues la salida completa de la consola cuando lo ejecutes.

Después de eso, seguimos con la actualización de la base maestra.
