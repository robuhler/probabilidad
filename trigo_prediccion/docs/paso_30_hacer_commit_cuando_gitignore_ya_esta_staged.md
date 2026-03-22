# Paso 30: hacer el commit cuando `.gitignore` ya está staged

Perfecto: ahora sí estás exactamente en el punto donde quería que llegaras.

## Lo que significa tu estado actual

Si `git status` te muestra esto:

```text
Changes to be committed:
  modified:   .gitignore
```

entonces eso significa que:

- el cambio en `.gitignore` ya fue agregado al stage,
- Git lo tiene listo,
- y ahora el siguiente paso natural es **hacer el commit**.

## Qué tenés que hacer ahora

Corré exactamente este comando:

```bash
git commit -m "Actualizar .gitignore del proyecto"
```

## Qué debería pasar

Git debería crear un nuevo commit con ese cambio.

Después de eso, si corrés `git status`, lo esperable es que el estado quede mucho más limpio.

## Después del commit

Corré:

```bash
git status
```

## Qué quiero que me mandes

Pegame la salida de estos dos comandos:

```bash
git commit -m "Actualizar .gitignore del proyecto"
git status
```

## Tranquilidad final

En este punto ya no estamos corrigiendo errores.

Ya estamos cerrando correctamente un cambio normal de Git: editar, stagear y commitear.
