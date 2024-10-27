# CARONTE CHALLENGE by EchoWave

## Inspiración
Este problema viene propuesto por la escuela de ingeniería de la UAB. Con el objetivo de mejorar a los alumnos sus notas académicas y su motivación.

## Qué hace
Se abre una aplicación con Python donde a través del ID de la clase y ID del alumno se puede predecir la nota que sacará de Final en base a sus entregas y exámenes anteriores y a otros casos de usos similares al del usuario.

## Cómo lo hemos desarrollado
La hemos construido mediante Notebook con tal de hacer un análisis de los datos exhaustivo con tal de dar la mejor información posible para entrenar a la IA. Para el entreno hemos usado Python con la librería Scikit-learn usando redes neuronales para precedir las notas de los alumnos.

## Retos encontrados
El análisis de los datos ha sido costoso en muchos aspectos, sobre todo habían muchas columnas que tenían incoherencias o no tenían valor suficiente para entrenar la IA. A la hora de hacer las estadísticas también hemos tenido que juntar muchos datasets con tal de mostrar estadísticas para la cantidad de aprobados, suspensos, % de entregas en relación con la nota final...

## Logros de los que estamos orgullosos
Hemos conseguido analizar y limpiar el dataset, encontrar correlaciones entre algunos atributos y la nota final.
Hemos desarrollado dos IA capaces de predecir la nota final del usuario, a través de sus datos académicos en Caronte.

## Qué hemos aprendido
- Hemos aprendido a analizar los datos otorgados.
- Organizar un workflow para trabajar en paralelo en IA.
- Aplicar modelos de IA a nuestros datos


## What's next for EchoWave Challenge Caronte
- Aumentar la database para una precisión mayor
- Interfaz mejorada y mas user-friendly
- Añadir funcionalidades como gráficos comparativos con la nota que el usuario desea obtener.
- Comprobar si otros modelos de IA pueden mejorar los resultados, y combinaciones de IA para un resultado más preciso.

## libaries
pandas
numpy
matplotlib
scikit-learn
