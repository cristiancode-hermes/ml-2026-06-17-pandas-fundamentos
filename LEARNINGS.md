# Learnings — 2026-06-17

## Qué se hizo
Primer proyecto de la ruta ML. Creamos una exploración completa del dataset de calidad de vinos tintos usando pandas. Aprendimos a cargar CSVs con separadores personalizados, explorar DataFrames, filtrar con condiciones, agrupar con groupby, y visualizar relaciones entre variables.

## Conceptos nuevos
- [x] pandas: pd.read_csv() con sep personalizado
- [x] Exploración: shape, head(), info(), describe()
- [x] Filtrado simple y compuesto (&, |)
- [x] groupby() con .mean(), .agg(), .size()
- [x] Visualización: countplot, boxplot, heatmap, pairplot, violinplot
- [x] Feature engineering básico: crear nuevas columnas
- [x] .query(), .sort_values(), .sample(), .rename()

## Dificultades encontradas
- El CSV usa ";" como separador, no "," — si no se especifica sep=';', pandas lee todo como una sola columna
- El dataset no tiene valores nulos (suerte para empezar), pero en proyectos reales esto no es normal
- seaborn tiene problemas con demasiadas columnas en pairplot (lento)

## Notas para el próximo proyecto
- Pasar a numpy: arrays, broadcasting, operaciones vectorizadas
- Relacionar numpy con pandas: cómo se complementan
- Usar algún dataset que justifique el uso intensivo de numpy (tal vez imágenes pequeñas o señales)
