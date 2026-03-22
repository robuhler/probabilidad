# Paso 18: hacer el primer commit local

Muy bien: ahora el estado de Git ya está mucho más prolijo.

## Lo que veo en tu `git status`

Ahora tenés staged solo esto:

- `.gitignore`
- `spot_trigo/inspect_cac_excel.py`

Y eso está bien para un primer commit simple.

## Qué NO vamos a hacer todavía

Por ahora no vamos a agregar:

- `.idea/`
- `main.py`
- `spot_trigo/inbox_excel/`

Porque esos son archivos de entorno local o archivos de trabajo que no queremos meter todavía en Git.

## Lo que quiero que hagas ahora

Corré este comando:

```bash
git commit -m "Primer commit del proyecto trigo_prediccion"
```

## Qué debería pasar

Git debería crear el primer commit local.

## Después de eso

Corré este comando:

```bash
git status
```

## Qué quiero que me mandes

Pegame la salida de estos dos comandos:

```bash
git commit -m "Primer commit del proyecto trigo_prediccion"
git status
```
