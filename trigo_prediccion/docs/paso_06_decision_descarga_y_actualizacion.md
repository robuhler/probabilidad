# Paso 6: decisión sobre la estrategia de descarga y actualización

Teníamos dos alternativas posibles:

1. pedirte que descargues manualmente el archivo histórico y que nuestros scripts automaticen el resto,
2. intentar automatizar tanto la descarga web como la actualización.

## Mi recomendación como profesor

Para esta etapa, recomiendo la **alternativa 1**:

- **descarga manual del Excel desde CAC/BCR**, y
- **automatización total desde el Excel hacia adelante**.

## Por qué recomiendo esto

### 1. Es más robusto
Si la web cambia un botón, un filtro o una interacción, no se rompe todo el proyecto.

### 2. Es mejor para un desarrollo ordenado en PyCharm
Primero resolvemos muy bien el corazón del flujo de datos.

### 3. Es más eficiente para el objetivo del MVP
Nuestro objetivo hoy no es automatizar una web compleja. Nuestro objetivo es tener una serie confiable, actualizable y con buen reporte.

### 4. Nos deja una puerta abierta a futuro
Cuando ya tengamos dominado el flujo desde Excel a reporte, podremos evaluar si conviene automatizar también la descarga desde la web.

## Decisión tomada para el proyecto

Por ahora vamos a trabajar así:

1. vos descargás el Excel histórico o actualizado desde CAC/BCR,
2. lo guardás en `spot_trigo/inbox_excel/`,
3. los scripts lo normalizan,
4. se actualiza la base maestra,
5. se genera el informe ejecutivo.
