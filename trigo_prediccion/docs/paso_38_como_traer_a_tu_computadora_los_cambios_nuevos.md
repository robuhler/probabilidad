# Paso 38: cómo traer a tu computadora los cambios nuevos

Perfecto: ahora ya estamos en la pregunta correcta.

## La respuesta corta

Para traer a tu computadora lo nuevo que haya en GitHub, vas a usar:

```bash
git pull
```

## Qué hace `git pull`

`git pull` le dice a Git:

> “traeme a esta carpeta local lo último que haya en el repositorio remoto”.

O sea:

- GitHub tiene una versión,
- tu computadora tiene otra copia,
- `git pull` baja a tu máquina lo que falte.

## Cuándo usarlo

Lo vas a usar cuando quieras actualizar tu copia local con cambios nuevos que ya estén subidos al remoto.

## Cómo hacerlo desde terminal

Parado dentro de la carpeta del proyecto, corré:

```bash
git pull
```

## Cómo hacerlo desde PyCharm

Si abrís la carpeta conectada al repo en PyCharm, podés usar:

- **Git → Pull**

Y PyCharm va a traer esos cambios a la carpeta local.

## La idea importante

Si yo o vos hacemos cambios y esos cambios llegan al repo remoto, entonces en tu compu los traés con:

```bash
git pull
```

## Lo que NO pasa automáticamente

No quiero que confundamos esto con magia.

No pasa esto:

- yo escribo algo en el chat,
- y tu computadora cambia sola.

Primero el cambio tiene que existir en el repo remoto.

Recién después vos lo bajás con `pull`.

## Flujo correcto a partir de ahora

Tu rutina normal va a ser algo así:

1. abrir tu proyecto en PyCharm,
2. hacer `git pull` para traer lo último,
3. trabajar sobre esos archivos,
4. hacer commit de tus cambios,
5. hacer `git push`.

## Qué carpeta tenés que usar

Muy importante: hacé `git pull` dentro de la carpeta que está conectada al repo.

No en cualquier carpeta parecida.

## Qué quiero que hagas ahora

Probá esto en tu carpeta del proyecto:

```bash
git pull
```

## Qué quiero que me mandes

Pegame la salida exacta de:

```bash
git pull
```

## Tranquilidad final

A partir de este punto, `git pull` es el comando clave para traer a tu computadora los cambios nuevos del repo.
