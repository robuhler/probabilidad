# Paso 23: si PowerShell interpreta `it status`

Perfecto: acá el problema no fue Git.

## Qué pasó realmente

Vos escribiste esto:

```bash
it status
```

pero el comando correcto era:

```bash
git status
```

Te faltó la letra **g** al principio.

## Por qué apareció ese mensaje raro

En PowerShell, `it` puede ser interpretado como otra cosa distinta de Git.

Por eso te apareció un mensaje relacionado con **Pester** y con `Describe block`.

Eso no tiene nada que ver con tu proyecto ni con el repositorio.

## Lo importante

No rompiste nada.

Simplemente PowerShell intentó ejecutar `it` como si fuera otro comando.

## Qué tenés que correr ahora

Corré exactamente esto:

```bash
git status
```

## Cómo evitar este error

Antes de apretar Enter, mirá que el comando empiece con:

- `git ...`

No con:

- `it ...`

## Qué deberías ver

Si Git está funcionando, deberías ver una salida parecida a una de estas:

```text
On branch main
nothing to commit, working tree clean
```

o bien algo indicando archivos modificados, staged o untracked.

## Qué quiero que me mandes

Pegame la salida exacta de:

```bash
git status
```

## Tranquilidad final

El mensaje de PowerShell sobre `The It command may only be used inside a Describe block` **no es un error del repo**.

Fue solo consecuencia de haber escrito `it status` en vez de `git status`.
