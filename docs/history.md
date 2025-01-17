# Historial de versiones

## 1.29.1 - 2019-12-18

- Bump de django-datajsonar a 0.6.5

## 1.29.0 - 2019-12-18

- Streamline de corrida manual de synchronizers
- Configuración de validación de distribuciones


## 1.28.13 - 2019-11-28

- Bump de series-tiempo-ar a 0.3.6

## 1.28.12 - 2019-11-26

- Bump de django-datajsonar a 0.6.3
- Bugfix en colapsos inferidos no aplicándose
- Agrego el nombre del nodo en reportes de indexación

## 1.28.11 - 2019-11-20

- Bump de django-datajsonar a 0.6.1, incluyendo funcionalidad de restaurar una configuración default de synchronizers
- Bugfix a corrida de indexación de metadatos para un nodo individual corriendo para todos los nodos

## 1.28.10 - 2019-11-20

- Fix de conflictos en borrado de datos durante indexación a Elasticsearch

## 1.28.9 - 2019-11-14

- Bump de series-tiempo-ar a 0.3.5

## 1.28.8 - 2019-11-12

- Bugfix de `representation_mode` como `percent_change_since_beginning_of_year` para que sea considerado porcentual

## 1.28.7 - 2019-11-05

- Bump de django-datajsonar a 0.5.1 (disponibiliza URLs de descarga de catálogos, auto whitelist de datasets federables)
- Bugfix en collapse_aggregation max/min para ciertas series tirando valores incorrectos
- Bugfix de distribuciones con múltiples índices de tiempo cargados (uno no presente) no indexandose
- Agregado de más newlines en reportes de errores para distinguir múltiples errores en una distribución

## 1.28.6 - 2019-10-18

- Agrego corridas de test de integración a UI del admin

## 1.28.5 - 2019-10-16

- Bugfix a dumps CSV no generándose si no existía metadato enriquecido de frecuencia de alguna de las series en la base

## 1.28.4 - 2019-10-15 

- Todo mail ahora es enviado con CCO al remitente
- Aplicación de heurística en el cálculo de cifras significativas de series, para corregir casos de errores de la representación decimal de los datos debido a la pérdida de precisión del punto flotante

## 1.28.3 - 2019-10-07

- Bugfix en collapse_aggregation no funcionando en casos de múltiples series con frecuencias diferentes
- Bugfix en precisión decimal de los datos indexados

## 1.28.2 - 2019-10-01

- Bump de django-datajsonar a 0.4.8
- Bugfix a tarea de indexación de datos corriendo para un único nodo

## 1.28.1 - 2019-09-24

- Bugfixes a metadato `significant_figures` que calculaba mal casos series de números enteros
- Bugfix en timeouts de indexación

## 1.28.0 - 2019/09/16

- Nuevo metadato enriquecido de series: `significant_figures`

## 1.27.1 - 2019/09/09

- Bugfix a agregaciones de collapse siendo ignoradas

## 1.27.0 - 2019/09/03

- Parámetros nuevos para `/search`: `sort` y `sort_by`
- Botones de acceso directo a acciones comunes en el admin de django

## 1.26.5 - 2019/08/20

- Indexación: Bugfixes y cambios en pydatajson para permitir lecturas concurrentes de catálogos en XLSX


## 1.26.4  - 2019/08/13

- Bugfix de `is_percentage` devolviendo valores incorrectos

## 1.26.3 - 2019/08/6 

- Bump de django-datjasonar a 0.4.3

## 1.26.2 - 2019/08/05

- Bugfix a metadatos de modos de representación de las series repetidos cuando se pedía una misma serie con distintos modos de representación

## 1.26.1 - 2019/07/25

- Modificaciones de Headers en responses para permitir usos de APIs en cualquier sitio (CORS)


## 1.26.0 - 2019/07/16

- Bump de series-tiempo-ar a 0.3.1
- Agrega parametro opcional `catalog_format` al endpoint de validaciones

## 1.25.0 - 2019/07/16

- Bump de django_datajsonar a 0.4.2
- Nuevo endpoint: /validate. Permite validar distribuciones de un catálogo de series de tiempo a partir de una URL y un identifier.

## 1.24.0 - 2019/07/02

- Recuperación de contraseña
- Mejora de descripción de títulos en consultas con formato CSV.
- Muestra de todos los errores de una distribución cuando falla

## 1.23.2 - 2019/06/24

- Fixes a pantalla del login

## 1.23.1 - 2019/06/18

- Filtra queries por método, descartando las de método `OPTIONS`.
- Estilos institucionales del login page.

## 1.23.0 - 2019/06/11

- Bump de versión de django_datajsonar con verificación de SSL a nivel nodo.
- Refactor menor de código para leer distribuciones desde el file system de la aplicación en vez de descargar desde la fuente original durante la generación de dumps.

## 1.22.0 - 2019/06/03

- Bugfix a consultas que devolvían datos vacíos cuando se pedía una serie con `collapse_aggregation` definido y sin `collapse`.

## 1.21.0 - 2019/05/15

- Cambios en la rutina de indexación de metadatos para hacer ciertos campos no obligatorios (`themeTaxonomy` de un catálogo fuente)
- La tabla de errores del reporte de indexación ahora viene ordenada según el ID del catálogo, y luego el ID de la distribución errónea


## 1.20.0 - 2019/05/13

- Validaciones adicionales en indexación de datos relacionadas con encoding de archivos en latin1
- Tabla de errores de distribuciones en reporte de indexación

## 1.19.0

- Fix de regresión de lectura de dataset identifiers durante la indexación de datos a Elasticsearch

## 1.18.0

- Fixes en indexación de distribuciones, no se verifica el certificado de SSL (necesario para obtener datos de algunos publicadores)
- Fix a lectura de series marcadas como no presentes

## 1.17.0

- Cambio caracter separador en /search: de ',' -> '||' (dos caracteres)

## 1.16.0

- Muestro ID de catalogos en reportes individuales
- Mejoras de manejo de errores de tareas asincronicas

## 1.15.0

- Bump de versión de django_datajsonar a 0.2.0, y adaptando la base de código para ser compatible con dicha versión
- Bugfix de indexación de metadatos: ahora se indexan todas las series _disponibles_ en vez de las _disponibles sin error_

## 1.14.0

- Bump de versión de django_datjasonar a 0.1.22
- Bugfix en cálculo de metadatos enriquecidos: ahora se calculan en todas las indexaciones, y no sólo cuando una distribución es actualizada

## 1.13.2

- Fix a mails no utilizando el campo from_email de la configuración dinámica.

## 1.13.1

- Fix a mails de test de integración mandandose múltiplies veces, y ocasionalmente con un attachment vacío
- Bump de versión micro de django_datajsonar
- Fix al callable_str de RunIntegrationTaskAdmin incorrecto

## 1.13.0

- Parametrización del índice de tiempo: no es más necesario utilizar un índice de tiempo con nombre `indice_tiempo` para indexar distribuciones
- Cambios de respuesta: percent_change cambia su nombre _verbose_ a `Variación porcentual período anterior`
- Validaciones adicionales en generación de dumps CSV y SQL

## 1.12.1

- Revert al uso de metadatos de consultas en el endpoint de búsqueda
- Revert al conteo de series en cada filtro de metadatos.
- Nuevo parámetro para `/search`: `aggregations` muestra el conteo de series relevantes para la búsqueda dada, desagregadas según los varios filtros posibles

## 1.12.0

- Bugfixes en indexación y respuesta de API series (#471, #473, #474)
- Administración de unidades de series, con atributo de si son porcentuales
- Conteo de series en cada filtro de metadatos
- Actualización de validaciones de series durante la indexación

## 1.11.0

Metadatos de consultas de las series: rutina de cálculo diaria, uso en dumps y en resultados de búsqueda de series

## 1.10.0

- Nuevos metadatos de series: `representation_mode` y `representation_mode_units`
- Borrado del croneado de tareas usado para metadatos, analytics y test de integración. Su funcionalidad quedó deprecada
por `Synchronizer` de `django_datajsonar`.

## 1.9.0

- Bump de la versión de `django_datajsonar` a 0.1.17, con mejoras de UX de Synchronizers
- Bump de la versión de `series-tiempo-ar` a 0.2.1, con una validación adicional para permitir distribuciones con series vacías, hasta cierta proporción.
- Agregados nuevos metadatos de series (`metadata=full` o `metadata=only`): `max_value`, `min_value`, `average`

## 1.8.0

- Integración con django_datajsonar: Uso de Synchronizers y Stages para correr
tareas asincrónicas de manera ordenada

## 1.7.0

- Optimizaciones de performance en dumps CSV 
- Indexación de datos: siempre se reindexan completamente las distribuciones (_refresh_)
- Test de integración y consistencia de los datos, a correr después de la indexación diaria.
- Bugfix de series sin datos cuando eran pedidas en un solo request
- Traducción parcial del panel de administración a español

## 1.6.0

Release con herramientas de administración para "refrescar" distribuciones de datos inconsistentes con su fuente.

## 1.5.1
Correcciones a dumps:

- Header faltante en hojas adicionales en dump XLSX
- Columnas y nombres de una tabla de dumps SQL
- Bugfix de generación de dump global XLSX
Mejoras de organización en el admin de django

## 1.5.0

- Nuevo parámetro `last`. Ver [documentación](https://series-tiempo-ar-api.readthedocs.io/es/latest/)
- Permito trailing slashes en URLs de descarga de dumps

## 1.4.3

- Fix de estabilidad de generación de dumps en general.

## 1.4.2

- Fix a tasks asincrónicas de dumps no corriendo correctamente cuando son generadas desde el admin

## 1.4.0

- Orden a filas de dump de metadatos
- No es más necesario setear dataset_identifier en distributciones para ser indexadas
- Se permiten csvs de distribuciones con encoding distinto a utf-8

## 1.3.3

- Callables de rqscheduler para dumps CSV y XLSX.

## 1.3.2

- Optimizaciones de memoria de generación dumps xlsx

## 1.3.1 

- Pequeño release con un fix a parseo de URLs de descarga de distribuciones


## 1.3.0 hotfix 2

- Hotfix para servir files de minio desde una ruta interna de la aplicación

## 1.3.0 hotfix 1

- Hotfixes de logging de dump

## 1.3.0

- Nueva generación de dumps en CSV, usando los datos cargados en postgres, y generando dumps individuales por catálogo.
- Borrado de datos en el endpoint de /search/ cuando una serie se borra de la base de datos

## 1.2.1

- Refactor e integración de generación de dumps de la base de datos de series de tiempo, para utilizar postgres en vez de Elasticsearch e integrar los archivos al filesystem distribuido

## 1.2.0

- Adopción de [semver](https://semver.org/) como sistema de versionado
- File system distribuido (minio)
- Optimizaciones en la UI del admin
- Display de mensajes de error en reportes de indexación

## 1.1.8

- Correcciones en importado de analytics para adaptarse a la nueva API paginada con cursor en api mgmt

## 1.1.7

- Cambio de nombres de respuesta de metadatos.
- Fixes de usabilidad del admin relacionado a administradores de nodos.
- Bugfixes en respuesta de /series


## 1.1.6

- Se aumenta el límite de series máximas por request a 40
- Revisión de nombres y agregado de metadatos en la respuesta de /series
- Cambio de nombre de parámetro de /search: offset -> start para consistencia con /series

## 1.1.5

- Análisis y tokenización de texto para la búsqueda de metadatos en /search. Permite reconocer palabras sin acento, entre otras cosas.
- Muestra de metadatos enriquecidos de las series pedidas en /series, cuando se pide la respuesta con metadata=full o metadata=only. Actualmente todos los valores devueltos son de tipo string, sujeto a cambios a futuro.

## 1.1.4

- Modificación de la respuesta de metadatos en search/: se agregan campos dataset.theme, dataset.source y
field.units. Además se cambia la respuesta de field.periodicity de formato legible por humanos a ISO8601

## 1.1.3

- Actualizaciones de django_datajsonar
- Se agregan aliases de catálogos para metadatos. Se puede configurar un alias para los filtros catalog_id que sea equivalente a filtrar por uno o más catálogos.

## 1.1.2

- Funcionalidades de importado histórico de analytics, y ampliación de los datos guardados de cada query

## 1.1.1

- Validación de catálogos leídos al generar reporte
- Fixes a los valores de reportes
- Fix de metadatos enriquecidos no mostrándose bien en /search/

## 1.1.0

- Nuevo formato de respuesta de metadatos tanto en /series como en /search
- Mejoras en visualizaciones del admin de django

## 1.0.18

- Mejoras al endpoint de búsqueda: nuevo parámetro catalog_id
- Mejoras al indexado de metadatos
- Configuración de importado de analytics desde un API gateway

## 1.0.17

Se pasa a usar `django_datajsonar` como dependencia directa para manejar las entidades procesadas de data.json de los nodos

## 1.0.16-1

Actualización de dependencias pydatajson==0.4.12

## 1.0.16

Actualización de validaciones para indexación

## 1.0.15

Release con:

- Resumen de reporte de indexación
- Detalle de cada entidad indexada como archivos adjuntos en el reporte
- Reimplementación de aggregations max y min
- Fechas en el dump de analytics se exportan en horario local

## 1.0.14

Mejoras al formato del reporte de indexación, junto con mensajes de error más descriptivos

## 1.0.13

Hotfix con fixes a comportamiento erróneo en queries de dos series iguales con distinto modo de representación + uso de caracter decimal no default

## 1.0.12

Release con:

- Permite generar reportes de indexación individuales por nodo
- Fixes a valores de los reportes (datasets actualizados, no actualizados)
- Mejoras de performance de la indexación de metadatos

## 1.0.11

Generación de reporte de indexación completo: Nuevos fields para catálogos, datasets, distribuciones y series.

## 1.0.10

- Mejoras en la generación de reportes de indexación, con más campos reportados.

## 1.0.9

- Mostrado de versión en la página principal del admin de Django
- Mejora del proceso de indexación y persistencia de las métricas obtenidas
- Bugfix para permitir que las series de tiempo puedan cambiar de distribución dentro de un mismo catálogo

## 1.0.8

Bugfixes:

- Correcciones a llamadas de series múltiples en orden descendiente
- Permito la exportación correcta de analytics a CSV en volúmenes grandes
- Correcciones a guardados de analytics erróneos

## 1.0.7

Endpoint de búsqueda de series: `/search`

## 1.0.6

Fixes a herramientas de administración:

- No se indexan metadatos de series y distribuciones pertenecientes a catálogos no marcados como indexables
- Finalización automática de la tarea de indexación si no hay datasets marcados como indexable
- Arreglos a borrados de croneado de tareas de indexación

## 1.0.3
Herramientas de administración:

- Configuración de que nodos y datasets se deben indexar
- Configuración del croneado de la tarea de indexación
- Generación de reportes de resultado de indexación por mail a los administradores 

## 1.0.0
Release inicial
