# Paso 11: actualizar la base maestra

Excelente: ya lograste generar el CSV normalizado.

Eso significa que ahora podemos pasar al siguiente paso.

## Objetivo de este paso

Tomar el CSV normalizado nuevo y sumarlo a la base histórica consolidada.

## Archivo que tenés que ejecutar

El script que hace esto es:

- `trigo_prediccion/spot_trigo/update_master.py`

## Forma más simple de usarlo en PyCharm

Ahora el script puede ejecutarse sin argumentos.

Si lo corrés así:

```bash
python trigo_prediccion/spot_trigo/update_master.py
```

va a buscar automáticamente este archivo:

- `trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv`

Y va a actualizar automáticamente este otro archivo:

- `trigo_prediccion/spot_trigo/master/precio_spot_trigo_master.csv`

## Resultado esperado

Si todo sale bien, deberías ver un mensaje parecido a este:

- `Base maestra actualizada: ... (N filas)`

## Qué quiero que me mandes después

Quiero que me pegues la salida completa de la consola.

Después seguimos con el informe automático.
