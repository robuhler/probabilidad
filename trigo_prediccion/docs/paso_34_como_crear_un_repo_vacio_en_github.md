# Paso 34: cómo crear un repo vacío en GitHub

Perfecto. Vamos a hacer solo esa parte.

## Qué significa “repo vacío”

Un repo vacío en GitHub es un repositorio nuevo que **no trae archivos iniciales creados por GitHub**.

O sea:

- sin `README.md`,
- sin `.gitignore`,
- sin licencia.

Eso es lo que queremos en tu caso, porque vos **ya tenés el proyecto armado en tu computadora**.

## Paso a paso en GitHub

### 1. Entrá a GitHub

Abrí:

```text
https://github.com
```

### 2. Iniciá sesión

Entrá con tu usuario.

### 3. Crear un repositorio nuevo

Tocá el botón:

- **New**

o

- **New repository**

según cómo te aparezca la interfaz.

### 4. Elegí el nombre

En **Repository name** escribí por ejemplo:

```text
trigo_prediccion
```

### 5. Elegí si va a ser público o privado

Podés elegir:

- **Public**
- o **Private**

Para este paso, cualquiera de las dos sirve.

### 6. MUY IMPORTANTE: dejarlo vacío

En la parte de inicialización, GitHub suele mostrar casillas como estas:

- **Add a README file**
- **Add .gitignore**
- **Choose a license**

En tu caso quiero que hagas esto:

- **NO marcar Add a README file**
- **NO elegir .gitignore**
- **NO elegir licencia**

## Cómo saber si quedó vacío correctamente

Si lo hiciste bien, GitHub te va a llevar a una pantalla que normalmente muestra instrucciones tipo:

```text
…or push an existing repository from the command line
```

Ese mensaje es una muy buena señal.

Significa justamente que el repo está listo para recibir tu proyecto local.

## Qué tenés que copiar después

En esa pantalla, GitHub te va a mostrar una URL del repositorio.

Algo como:

```text
https://github.com/tu_usuario/trigo_prediccion.git
```

Esa es la URL que después vas a usar en:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

## Qué quiero que me mandes

Cuando termines este paso, mandame una de estas dos cosas:

1. la URL del repo,
2. o una captura / texto de la pantalla donde GitHub te muestra `push an existing repository from the command line`.

## Tranquilidad final

Si dejás el repo sin README, sin `.gitignore` y sin licencia, entonces lo estás creando **exactamente como lo necesitamos**.
