# Paso 3: fuente del precio spot del trigo

En esta etapa vamos a trabajar únicamente con la fuente del **precio spot del trigo**.

## Fuente elegida

La fuente elegida para esta variable es la página de consultas de la Cámara Arbitral de Cereales de la Bolsa de Comercio de Rosario.

## Criterio acordado para la descarga

Dentro de las opciones de precios, vamos a utilizar:

- **Precio Pizarra y Estimativo**.

La lógica es correcta: cuando no existe precio de pizarra, la BCR publica un precio estimativo y eso nos ayuda a no perder observaciones útiles en la serie histórica.

## Qué queremos resolver en esta etapa

Con esta variable queremos dejar armado un proceso que permita:

1. descargar el histórico,
2. incorporar nuevas observaciones,
3. actualizar una base maestra,
4. generar un informe automático con tabla y gráficos.

## Importante

Como estamos trabajando paso a paso, todavía no vamos a tocar las demás variables.

Primero dejamos sólido el proceso del precio spot.
