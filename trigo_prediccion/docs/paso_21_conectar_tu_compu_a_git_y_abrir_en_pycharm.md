# Paso 21: conectar tu compu a Git y abrir el proyecto en PyCharm

Este paso está pensado exactamente para esta necesidad:

> “Quiero tener en mi compu y en mi PyCharm todos los archivos creados en este proyecto”.

## Idea simple

Para lograr eso necesitás trabajar con una carpeta que esté conectada a Git.

La forma más práctica es usar GitHub como repositorio remoto y después abrir ese repo en PyCharm.

## Opción recomendada: clonar el repositorio en PyCharm

Si ya tenés el proyecto subido a GitHub, hacé esto:

### Paso 1
Copiá la URL del repositorio.

Ejemplo:

```text
https://github.com/tu_usuario/trigo_prediccion.git
```

### Paso 2
Abrí PyCharm.

### Paso 3
En la pantalla inicial elegí:

- **Get from VCS**

### Paso 4
Pegá la URL del repositorio.

### Paso 5
Elegí la carpeta destino en tu computadora.

### Paso 6
Tocá **Clone**.

### Paso 7
Cuando termine, abrí ese proyecto.

Y listo: esa carpeta ya queda conectada a Git.

## Qué vas a poder hacer después

Desde ese momento, en PyCharm vas a poder:

- ver todos los archivos del repo,
- hacer commits,
- hacer `pull` para bajar cambios,
- hacer `push` para subir tus cambios.

## Si preferís hacerlo por terminal

También podés clonar así:

```bash
git clone URL_DEL_REPOSITORIO
```

Después abrís en PyCharm la carpeta descargada.

## Si el proyecto todavía no está en GitHub

Entonces primero necesitás subirlo.

Desde la carpeta principal del proyecto local corré:

```bash
git init
git add .
git commit -m "Inicio del proyecto trigo_prediccion"
git remote add origin URL_DEL_REPOSITORIO
git branch -M main
git push -u origin main
```

Después de eso ya podés usar la opción de clonado en PyCharm.

## Cómo traer cambios nuevos más adelante

Si el proyecto ya está abierto en PyCharm y querés bajar cambios nuevos del repositorio:

### Opción PyCharm
Usá la opción de:

- **Git → Pull**

### Opción terminal
Dentro de la carpeta del proyecto corré:

```bash
git pull
```

## Error común que quiero evitarte

No mezcles muchas carpetas distintas del mismo proyecto.

Mi recomendación es trabajar siempre sobre:

- **la carpeta que clonaste desde GitHub**

Así PyCharm, Git y tus archivos quedan todos apuntando al mismo lugar.

## Qué quiero que hagas ahora

Elegí uno de estos dos caminos:

1. **si ya tenés una URL del repo**, clonarlo en PyCharm,
2. **si todavía no lo subiste a GitHub**, subirlo primero y después clonarlo.

Y si querés, en el próximo mensaje te guío con los comandos exactos según tu caso.
