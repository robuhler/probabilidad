# Paso 27: si en PyCharm aparece algo como `RStudio files`

Perfecto: entiendo por qué eso te hace ruido.

Y quiero aclararlo bien:

## No, eso no significa que `trigo_prediccion` sea un proyecto de RStudio

El subproyecto que estamos trabajando ahora es este:

- `trigo_prediccion/`

Y para este trabajo lo que importan son tus archivos de Python, tus docs y la carpeta `spot_trigo/`.

## Entonces, ¿por qué podría aparecer algo como `RStudio files`?

Porque el repositorio raíz donde vive este subproyecto también contiene archivos viejos o ajenos a este flujo.

Por ejemplo, si existe un archivo `.Rproj` en la raíz del repo, PyCharm puede mostrar alguna referencia visual o categorización relacionada con RStudio.

## Lo importante para vos

Eso **no cambia** el objetivo del subproyecto ni significa que yo te esté mandando a trabajar sobre el curso viejo.

Para este proyecto, quiero que ignores todo eso y te concentres solo en:

- `trigo_prediccion/README.md`
- `trigo_prediccion/docs/`
- `trigo_prediccion/spot_trigo/`

## Cómo leer correctamente la situación

### Si ves `RStudio files`
Interpretalo como una referencia del entorno o del repo raíz.

### Si estás dentro de `trigo_prediccion/`
Entonces estás en el lugar correcto para este proyecto.

## Qué quiero dejarte bien claro

No quiero que tomes como guía el curso viejo, Udemy, ni un proyecto anterior.

Quiero que tomes como guía **solo** el subproyecto `trigo_prediccion/`.

## Qué quiero que hagas ahora

Si PyCharm te muestra algo confuso del repo raíz, ignoralo por ahora.

Y seguí trabajando únicamente dentro de:

```text
trigo_prediccion/
```

## Tranquilidad final

Que aparezca un texto como `RStudio files` no significa que este proyecto esté mal.

Solo significa que el repositorio contenedor tiene otras cosas además de `trigo_prediccion`.
