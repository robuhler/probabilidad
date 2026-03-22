# Proyecto: predicción del precio del trigo en Argentina

## Aclaración de alcance

Este subproyecto `trigo_prediccion/` hay que leerlo como un espacio **independiente**.

Si en algún momento PyCharm o el repositorio raíz muestran referencias a cosas como curso, Udemy o incluso algo relacionado con RStudio, **eso no forma parte del trabajo operativo de `trigo_prediccion`**.

Para este proyecto, lo único importante es esta carpeta:

- `trigo_prediccion/`

Todo lo demás del repositorio raíz puede ignorarse para el trabajo diario de este flujo.

A partir de ahora voy a acompañarte **como profesor**, avanzando paso a paso y sin adelantarnos.

## Regla de trabajo

No vamos a construir todo el proyecto de una vez.

En cada etapa vamos a hacer solo tres cosas:

1. entender qué estamos decidiendo,
2. dejar una definición simple y correcta,
3. recién después pasar al paso siguiente.

## Estado actual del proyecto

Ya cerramos el **Paso 1** y el **Paso 2**.

La definición acordada del problema quedó así:

> Vamos a predecir el **precio spot del trigo** en Argentina, con frecuencia **semanal** y un horizonte de **4 semanas**, para ayudar a la toma de decisiones de compra y planificación en un **molino harinero**.

Las variables iniciales del MVP quedaron acordadas así:

1. precio spot del trigo rezagado,
2. precio futuro del trigo,
3. precio internacional de referencia,
4. tipo de cambio,
5. producción o condición de campaña.

Además, dejamos anotadas para una etapa futura dos variables de calidad muy importantes para el molino:

- **gluten**,
- **PH**.

Por ahora esas variables quedan fuera del MVP inicial, pero las vamos a recordar para evaluarlas más adelante.

## En qué nos vamos a enfocar ahora

Ahora vamos a trabajar **solo con la primera variable**:

- **precio spot del trigo**.

Hasta no dejar resuelto el flujo de esta variable, no vamos a pasar a las demás.

## Qué tenés que leer ahora

- `trigo_prediccion/docs/paso_00_como_vamos_a_trabajar.md`
- `trigo_prediccion/docs/paso_01_definir_objetivo.md`
- `trigo_prediccion/docs/paso_02_variables_iniciales.md`
- `trigo_prediccion/docs/paso_03_fuente_precio_spot.md`
- `trigo_prediccion/docs/paso_04_actualizacion_y_reporte.md`
- `trigo_prediccion/docs/paso_05_estructura_pycharm.md`
- `trigo_prediccion/docs/paso_06_decision_descarga_y_actualizacion.md`
- `trigo_prediccion/docs/paso_07_si_falla_el_adjunto_excel.md`
- `trigo_prediccion/docs/paso_08_mapa_de_carpetas_y_scripts.md`
- `trigo_prediccion/docs/paso_09_estructura_real_excel_cac.md`
- `trigo_prediccion/docs/paso_10_normalizar_excel_real.md`
- `trigo_prediccion/docs/paso_11_actualizar_base_maestra.md`
- `trigo_prediccion/docs/paso_12_como_llevar_los_cambios_a_tu_pycharm.md`
- `trigo_prediccion/docs/paso_13_sincronizar_con_git.md`
- `trigo_prediccion/docs/paso_14_verificar_si_tenes_git.md`
- `trigo_prediccion/docs/paso_15_inicializar_git_local.md`
- `trigo_prediccion/docs/paso_16_ordenar_git_status_local.md`
- `trigo_prediccion/docs/paso_17_corregir_gitignore_y_limpiar_stage.md`
- `trigo_prediccion/docs/paso_18_hacer_primer_commit_local.md`
- `trigo_prediccion/docs/paso_19_configurar_identidad_git.md`
- `trigo_prediccion/docs/paso_20_interpretar_untracked_despues_del_primer_commit.md`
- `trigo_prediccion/docs/paso_21_conectar_tu_compu_a_git_y_abrir_en_pycharm.md`
- `trigo_prediccion/docs/paso_22_si_git_add_no_agrega_nada.md`
- `trigo_prediccion/docs/paso_23_si_powerShell_interpreta_it_status.md`
- `trigo_prediccion/docs/paso_24_sacar_del_stage_archivos_locales_no_deseados.md`
- `trigo_prediccion/docs/paso_25_si_git_status_muestra_solo_untracked_files.md`
- `trigo_prediccion/docs/paso_26_que_significa_el_icono_de_pycharm_con_circulo_y_raya.md`
- `trigo_prediccion/docs/paso_27_si_aparece_rstudio_files_en_pycharm.md`
- `trigo_prediccion/docs/paso_28_si_gitignore_aparece_como_modified.md`
- `trigo_prediccion/docs/paso_29_si_gitignore_ya_esta_en_changes_to_be_committed.md`
- `trigo_prediccion/docs/paso_30_hacer_commit_cuando_gitignore_ya_esta_staged.md`
- `trigo_prediccion/docs/paso_31_si_git_status_dice_working_tree_clean.md`
- `trigo_prediccion/docs/paso_32_conectar_pycharm_a_un_repo_remoto_para_actualizar_cambios.md`
- `trigo_prediccion/docs/paso_33_ruta_b_crear_repo_en_github_y_conectarlo_a_pycharm.md`
- `trigo_prediccion/docs/paso_34_como_crear_un_repo_vacio_en_github.md`
- `trigo_prediccion/docs/paso_35_si_git_dice_invalid_refspec_al_conectar_github.md`
- `trigo_prediccion/docs/paso_36_si_github_abre_sign_in_al_hacer_push.md`
- `trigo_prediccion/docs/paso_37_si_git_push_dice_everything_up_to_date.md`
- `trigo_prediccion/docs/paso_38_como_traer_a_tu_computadora_los_cambios_nuevos.md`
- `trigo_prediccion/spot_trigo/README.md`

## Aclaración importante sobre tu PyCharm

Tu proyecto local en PyCharm **no se actualiza automáticamente** con lo que yo escribo acá.

Si querés que un cambio exista en tu computadora, tenés que:

- copiar el archivo nuevo o actualizado, o
- sincronizarlo con Git si estuvieras trabajando con un repo conectado.

Para eso dejé esta guía:

- `trigo_prediccion/docs/paso_12_como_llevar_los_cambios_a_tu_pycharm.md`
- `trigo_prediccion/docs/paso_13_sincronizar_con_git.md`
- `trigo_prediccion/docs/paso_14_verificar_si_tenes_git.md`
- `trigo_prediccion/docs/paso_15_inicializar_git_local.md`
- `trigo_prediccion/docs/paso_16_ordenar_git_status_local.md`
- `trigo_prediccion/docs/paso_17_corregir_gitignore_y_limpiar_stage.md`
- `trigo_prediccion/docs/paso_18_hacer_primer_commit_local.md`
- `trigo_prediccion/docs/paso_19_configurar_identidad_git.md`
- `trigo_prediccion/docs/paso_20_interpretar_untracked_despues_del_primer_commit.md`
- `trigo_prediccion/docs/paso_21_conectar_tu_compu_a_git_y_abrir_en_pycharm.md`
- `trigo_prediccion/docs/paso_22_si_git_add_no_agrega_nada.md`
- `trigo_prediccion/docs/paso_23_si_powerShell_interpreta_it_status.md`
- `trigo_prediccion/docs/paso_24_sacar_del_stage_archivos_locales_no_deseados.md`
- `trigo_prediccion/docs/paso_25_si_git_status_muestra_solo_untracked_files.md`
- `trigo_prediccion/docs/paso_26_que_significa_el_icono_de_pycharm_con_circulo_y_raya.md`
- `trigo_prediccion/docs/paso_27_si_aparece_rstudio_files_en_pycharm.md`
- `trigo_prediccion/docs/paso_28_si_gitignore_aparece_como_modified.md`
- `trigo_prediccion/docs/paso_29_si_gitignore_ya_esta_en_changes_to_be_committed.md`
- `trigo_prediccion/docs/paso_30_hacer_commit_cuando_gitignore_ya_esta_staged.md`
- `trigo_prediccion/docs/paso_31_si_git_status_dice_working_tree_clean.md`
- `trigo_prediccion/docs/paso_32_conectar_pycharm_a_un_repo_remoto_para_actualizar_cambios.md`
- `trigo_prediccion/docs/paso_33_ruta_b_crear_repo_en_github_y_conectarlo_a_pycharm.md`
- `trigo_prediccion/docs/paso_34_como_crear_un_repo_vacio_en_github.md`
- `trigo_prediccion/docs/paso_35_si_git_dice_invalid_refspec_al_conectar_github.md`
- `trigo_prediccion/docs/paso_36_si_github_abre_sign_in_al_hacer_push.md`
- `trigo_prediccion/docs/paso_37_si_git_push_dice_everything_up_to_date.md`
- `trigo_prediccion/docs/paso_38_como_traer_a_tu_computadora_los_cambios_nuevos.md`

## Dónde están los scripts del precio spot

Todos los scripts operativos de esta primera variable están dentro de:

- `trigo_prediccion/spot_trigo/`

El script que te pedí correr para inspeccionar el Excel está en:

- `trigo_prediccion/spot_trigo/inspect_cac_excel.py`

## Si alguna explicación te resulta confusa

Tenés todo el derecho de frenar y pedirme que vuelva a explicarlo más simple.

Para eso dejé dos guías nuevas:

- `trigo_prediccion/docs/paso_00_como_vamos_a_trabajar.md`
- `trigo_prediccion/docs/paso_08_mapa_de_carpetas_y_scripts.md`
- `trigo_prediccion/docs/paso_09_estructura_real_excel_cac.md`
- `trigo_prediccion/docs/paso_10_normalizar_excel_real.md`
- `trigo_prediccion/docs/paso_11_actualizar_base_maestra.md`
- `trigo_prediccion/docs/paso_12_como_llevar_los_cambios_a_tu_pycharm.md`
- `trigo_prediccion/docs/paso_13_sincronizar_con_git.md`
- `trigo_prediccion/docs/paso_14_verificar_si_tenes_git.md`
- `trigo_prediccion/docs/paso_15_inicializar_git_local.md`
- `trigo_prediccion/docs/paso_16_ordenar_git_status_local.md`
- `trigo_prediccion/docs/paso_17_corregir_gitignore_y_limpiar_stage.md`
- `trigo_prediccion/docs/paso_18_hacer_primer_commit_local.md`
- `trigo_prediccion/docs/paso_19_configurar_identidad_git.md`
- `trigo_prediccion/docs/paso_20_interpretar_untracked_despues_del_primer_commit.md`
- `trigo_prediccion/docs/paso_21_conectar_tu_compu_a_git_y_abrir_en_pycharm.md`
- `trigo_prediccion/docs/paso_22_si_git_add_no_agrega_nada.md`
- `trigo_prediccion/docs/paso_23_si_powerShell_interpreta_it_status.md`
- `trigo_prediccion/docs/paso_24_sacar_del_stage_archivos_locales_no_deseados.md`
- `trigo_prediccion/docs/paso_25_si_git_status_muestra_solo_untracked_files.md`
- `trigo_prediccion/docs/paso_26_que_significa_el_icono_de_pycharm_con_circulo_y_raya.md`
- `trigo_prediccion/docs/paso_27_si_aparece_rstudio_files_en_pycharm.md`
- `trigo_prediccion/docs/paso_28_si_gitignore_aparece_como_modified.md`
- `trigo_prediccion/docs/paso_29_si_gitignore_ya_esta_en_changes_to_be_committed.md`
- `trigo_prediccion/docs/paso_30_hacer_commit_cuando_gitignore_ya_esta_staged.md`
- `trigo_prediccion/docs/paso_31_si_git_status_dice_working_tree_clean.md`
- `trigo_prediccion/docs/paso_32_conectar_pycharm_a_un_repo_remoto_para_actualizar_cambios.md`
- `trigo_prediccion/docs/paso_33_ruta_b_crear_repo_en_github_y_conectarlo_a_pycharm.md`
- `trigo_prediccion/docs/paso_34_como_crear_un_repo_vacio_en_github.md`
- `trigo_prediccion/docs/paso_35_si_git_dice_invalid_refspec_al_conectar_github.md`
- `trigo_prediccion/docs/paso_36_si_github_abre_sign_in_al_hacer_push.md`
- `trigo_prediccion/docs/paso_37_si_git_push_dice_everything_up_to_date.md`
- `trigo_prediccion/docs/paso_38_como_traer_a_tu_computadora_los_cambios_nuevos.md`

## Cómo quiero que trabajemos juntos

Yo te voy a guiar con preguntas y explicaciones cortas.

Vos vas a ir tomando decisiones una por una.

Ahora pasamos al trabajo operativo del **precio spot del trigo**: fuente, actualización y reporte ejecutivo.
