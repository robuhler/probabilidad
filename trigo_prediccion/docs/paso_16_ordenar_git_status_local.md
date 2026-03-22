# Paso 16: ordenar el estado de Git en tu proyecto local

Perfecto: la salida de `git status` ya nos mostró exactamente qué está pasando.

## Lo importante que veo en tu salida

### 1. Git ya está inicializado
Eso está bien.

### 2. PyCharm te agregó archivos propios
Aparecen archivos dentro de:

- `.idea/`

Esos archivos no son parte del proyecto de datos. Son archivos internos de PyCharm.

### 3. Hay un Excel descargado
Aparece:

- `spot_trigo/inbox_excel/archivo_descargado.xlsx`

Eso está bien como archivo de trabajo local, pero **no conviene versionarlo con Git**.

### 4. Hay un archivo mal ubicado
Aparece esto:

- `spot_trigo/inbox_excel/normalize_cac_excel.py`

Ese archivo **no debería estar dentro de `inbox_excel/`**.

La carpeta `inbox_excel/` es solo para archivos Excel descargados.

El script correcto tiene que estar en:

- `spot_trigo/normalize_cac_excel.py`

### 5. También aparece un CSV generado dentro de una ruta incorrecta
Aparece algo como:

- `spot_trigo/inbox_excel/trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv`

Eso también está mal ubicado.

Los CSV normalizados deberían quedar en:

- `spot_trigo/normalized/`

no dentro de `inbox_excel/`.

## Qué vamos a hacer ahora

Vamos a hacer dos cosas:

1. ignorar con Git los archivos locales y generados,
2. corregir los archivos que quedaron guardados en carpetas equivocadas.

## Archivo nuevo importante

Agregué este archivo:

- `trigo_prediccion/.gitignore`

Ese archivo está pensado específicamente para tu proyecto local, si trabajás con `trigo_prediccion/` como carpeta principal del repo.

## Qué quiero que hagas ahora

### Paso 1
Asegurate de copiar `trigo_prediccion/.gitignore` dentro de la carpeta raíz de tu proyecto local.

### Paso 2
Borrá o mové estos archivos mal ubicados:

- `spot_trigo/inbox_excel/normalize_cac_excel.py`
- `spot_trigo/inbox_excel/trigo_prediccion/spot_trigo/normalized/precio_spot_trigo_normalizado.csv`

### Paso 3
En la terminal del proyecto corré:

```bash
git rm -r --cached .idea
```

Si te da error porque algún archivo no está staged, no pasa nada: seguimos.

### Paso 4
Corré este comando:

```bash
git status
```

## Qué quiero que me pegues

Quiero que me pegues la nueva salida de:

```bash
git status
```

Después seguimos con el siguiente paso para dejar el proyecto limpio y ordenado.
