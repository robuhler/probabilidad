# Paso 35: si Git dice `invalid refspec` al conectar GitHub

Perfecto: ya veo qué pasó.

## Qué pasó realmente

En tu terminal apareció algo como esto:

```text
git push -u origin maingit remote add origin https://github.com/robuhler/trigo_prediccion.git
fatal: invalid refspec 'https://github.com/robuhler/trigo_prediccion.git'
```

Eso significa que **dos comandos quedaron pegados en una sola línea**.

Git intentó leer todo eso como si fuera parte del mismo comando, y por eso apareció el error `invalid refspec`.

## Lo importante

No significa que GitHub esté mal.

No significa que tu repo esté roto.

Significa solamente que los comandos no se ejecutaron por separado.

## Cómo hay que hacerlo correctamente

Quiero que corras estos comandos **uno por uno**, cada uno con Enter propio.

### Comando 1

```bash
git remote add origin https://github.com/robuhler/trigo_prediccion.git
```

### Comando 2

```bash
git branch -M main
```

### Comando 3

```bash
git push -u origin main
```

## Muy importante

No pegues esto todo junto en una misma línea:

```text
git push -u origin maingit remote add origin ...
```

Cada comando va separado.

## Qué debería pasar ahora

Si `origin` todavía no fue agregado correctamente, el primer comando lo va a crear.

Después:

- `git branch -M main` asegura el nombre de la rama,
- `git push -u origin main` sube el proyecto a GitHub.

## Si el primer comando dice que `origin` ya existe

Entonces no lo repitas.

En ese caso seguí solo con:

```bash
git branch -M main
git push -u origin main
```

## Qué quiero que me mandes

Pegame la salida exacta de estos comandos, ejecutados por separado:

```bash
git remote add origin https://github.com/robuhler/trigo_prediccion.git
git branch -M main
git push -u origin main
```

## Tranquilidad final

El error `invalid refspec` acá no fue un problema del repo.

Fue solo un problema de haber pegado mal los comandos en la terminal.
