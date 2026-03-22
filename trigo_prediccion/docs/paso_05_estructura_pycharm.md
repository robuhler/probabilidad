# Paso 5: estructura recomendada para trabajar en PyCharm

Como querés desarrollar este proyecto en tu computadora y en PyCharm, necesitamos una estructura clara y estable.

## Estructura recomendada para esta etapa

```text
trigo_prediccion/
├── README.md
├── requirements.txt
├── docs/
│   ├── paso_01_definir_objetivo.md
│   ├── paso_02_variables_iniciales.md
│   ├── paso_03_fuente_precio_spot.md
│   ├── paso_04_actualizacion_y_reporte.md
│   ├── paso_05_estructura_pycharm.md
│   └── paso_06_decision_descarga_y_actualizacion.md
└── spot_trigo/
    ├── README.md
    ├── inbox_excel/
    ├── normalized/
    ├── master/
    ├── reports/
    ├── samples/
    ├── normalize_cac_excel.py
    ├── update_master.py
    ├── generate_report.py
    └── run_pipeline.py
```

## Qué va en cada carpeta

### `inbox_excel/`
Acá vas a guardar los archivos Excel descargados desde la web de CAC/BCR.

### `normalized/`
Acá van a quedar los CSV ya normalizados, listos para consolidar.

### `master/`
Acá va la serie histórica consolidada del precio spot.

### `reports/`
Acá va a quedar el informe ejecutivo automático.

## Orden de trabajo en PyCharm

1. descargar Excel desde la web,
2. guardar el archivo en `inbox_excel/`,
3. ejecutar `normalize_cac_excel.py`,
4. ejecutar `run_pipeline.py`,
5. revisar el reporte en `reports/`.
