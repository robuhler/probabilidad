# Paso 7: qué hacer si no podés adjuntar el Excel

Sí, puede pasar.

Aunque el archivo sea pequeño, a veces la carga falla por el navegador, la sesión, el canal de subida o el formato del archivo.

## ¿Es normal?

No debería pasar siempre, pero sí puede pasar ocasionalmente.

No significa que el archivo esté mal.

## Mejor alternativa para seguir trabajando

Como queremos desarrollar esto en tu computadora y en PyCharm, la mejor alternativa es esta:

1. vos corrés un script local para inspeccionar el Excel,
2. me compartís la salida de ese script,
3. con eso yo ajusto el normalizador al archivo real.

## Script recomendado para inspeccionar el Excel

Usá:

```bash
python trigo_prediccion/spot_trigo/inspect_cac_excel.py --input "ruta/al/archivo.xlsx"
```

Ese script te va a mostrar:

- el nombre de las hojas,
- las primeras filas con contenido,
- una vista preliminar de los encabezados.

## Otras alternativas si sigue fallando la carga

### Opción A
Mandarme por texto:

- nombre de la hoja,
- nombres exactos de las columnas,
- primeras 5 a 10 filas.

### Opción B
Mandarme una captura de pantalla del Excel abierto.

### Opción C
Guardar una copia en CSV y compartir el contenido de las primeras filas.

### Opción D
Copiar y pegar en el chat solo la fila de encabezados y unas pocas filas de ejemplo.

## Mi recomendación como profesor

La mejor opción es correr `inspect_cac_excel.py` en tu PyCharm y pegarme la salida.

Es la manera más prolija, rápida y exacta de avanzar al siguiente paso.
