# code-challeng-latam-airlines
El desafío consiste en tomar el trabajo de un Data Scientist y sugerir mejoras de este mismo
Problema:



El problema que trató de resolver el DS fue predecir la probabilidad de atraso de los vuelos que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso utilizó un dataset de datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL. 
Para cada vuelo se cuenta con la siguiente información:

Fecha-I: Fecha y hora programada del vuelo. 
Vlo-I: Número de vuelo programado.
Ori-I: Código de ciudad de origen programado. 
Des-I: Código de ciudad de destino programado. 
Emp-I: Código aerolínea de vuelo programado. 
Fecha-O: Fecha y hora de operación del vuelo. 
Vlo-O: Número de vuelo de operación del vuelo. 
Ori-O: Código de ciudad de origen de operación 
Des-O: Código de ciudad de destino de operación. 
Emp-O: Código aerolínea de vuelo operado.
DIA: Día del mes de operación del vuelo.
MES: Número de mes de operación del vuelo. 
AÑO: Año de operación del vuelo.
DIANOM: Día de la semana de operación del vuelo. 
TIPOVUELO : Tipo de vuelo, I =Internacional, N =Nacional. 
OPERA: Nombre de aerolínea que opera.
SIGLAORI: Nombre ciudad origen.
SIGLADES: Nombre ciudad destino.

En el jupyter vas a encontrar:

¿Cómo se distribuyen los datos?

Generación de columnas adicionales:

Temporada_alta: 1 si Fecha-I está entre 15-Dic y 3-Mar, o 15-Jul y 31-Jul, o 11-Sep y 30-Sep, 0 si no.

dif_min: diferencia en minutos entre Fecha-O y Fecha-I.

atraso_15: 1 si dif_min > 15, 0 si no.

periodo_dia: mañana (entre 5:00 y 11:59), tarde (entre 12:00 y 18:59) y noche (entre 19:00 y 4:59), en base a Fecha-I.

¿Cómo se compone la tasa de atraso por destino, aerolínea, mes del año, día de la semana, temporada, tipo de vuelo? 

Entrenamiento de uno o varios modelos para estimar la probabilidad de atraso de un vuelo (target atraso_15).

Evaluación del performance del o los modelos.


# Desafí0

Como ML Engineer, tu desafío consiste en tomar el trabajo de este Data Scientist y exponerlo para que sea explotado por un sistema:

Escoger el modelo que a tu criterio tenga un mejor performance, argumentando la decisión.
Implementar mejoras sobre el modelo escogiendo la o las técnicas que prefieras. 
Exponer el modelo seleccionado como API REST para ser expuesto.
Hacer pruebas de estrés a la API con el modelo expuesto con al menos 50.000 requests durante 45 segundos. Para esto debes utilizar esta herramienta y presentar las métricas obtenidas. 

¿Cómo podrías mejorar el performance de las pruebas anteriores?




