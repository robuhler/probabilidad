# Paso 19: configurar tu identidad en Git

Perfecto: ahora apareció un error muy normal la primera vez que uno quiere hacer un commit.

## Qué significa el error

Git te está diciendo que todavía no sabe:

- cuál es tu nombre,
- y cuál es tu email.

Sin eso, no te deja crear commits.

## Lo que quiero que hagas ahora

Como estamos trabajando paso a paso, te recomiendo configurar estos datos **solo para este proyecto**, no de forma global todavía.

Corré estos dos comandos reemplazando tus datos:

```bash
git config user.name "Tu Nombre"
git config user.email "tu_email@example.com"
```

## Ejemplo

Si quisieras usar un nombre y un email cualquiera, sería algo así:

```bash
git config user.name "Roberto H"
git config user.email "roberto@example.com"
```

## Después de eso

Volvé a correr:

```bash
git commit -m "Primer commit del proyecto trigo_prediccion"
```

Y después:

```bash
git status
```

## Qué quiero que me mandes

Pegame la salida de estos dos comandos:

```bash
git commit -m "Primer commit del proyecto trigo_prediccion"
git status
```

## Importante

En este paso no hace falta usar `--global`.

Primero quiero que funcione bien dentro de este proyecto local.
