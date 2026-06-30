# 🎯 Fundamentos de pandas con Datos Reales de Vinos

**Nivel:** 1 — Fundamentos Python para ML  
**Skill:** pandas (DataFrames, CSV, filtros, groupby)  
**Datos:** Wine Quality Dataset (UCI) — 1599 vinos tintos portugueses

---

## 📖 Qué vas a aprender

**pandas** es la librería más importante para trabajar con datos en Python. Piensa en ella como "Excel con superpoderes". En este proyecto aprenderás a:

- **Cargar** un dataset real desde un archivo CSV
- **Explorar** los datos: ¿cuántas filas, qué columnas, qué tipo de datos?
- **Filtrar** filas con condiciones (como buscar en Excel pero programáticamente)
- **Agrupar** datos con `groupby` para calcular promedios y estadísticas por categoría
- **Visualizar** relaciones entre variables para entender los datos
- **Crear** nuevas columnas (feature engineering básico)

### ¿Por qué este dataset?

El dataset de calidad de vinos tintos es perfecto para empezar porque:
- ✅ Tiene datos reales, no inventados
- ✅ Es limpio (sin valores nulos)
- ✅ Las variables tienen sentido químico (pH, alcohol, acidez)
- ✅ La variable objetivo (calidad) es clara
- ✅ Hay relaciones interesantes entre variables para descubrir

---

## 🧪 Código paso a paso

### Paso 1: Importar librerías
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

- **pandas** → El corazón del proyecto, para DataFrames
- **numpy** → Operaciones numéricas (medias, desviaciones)
- **matplotlib/seaborn** → Para hacer gráficos y "ver" los datos

### Paso 2: Cargar los datos
```python
df = pd.read_csv('data/winequality-red.csv', sep=';')
```
El `sep=';'` es clave: los CSVs europeos usan punto y coma porque la coma se usa como decimal.

### Paso 3: Exploración inicial
- `df.shape` → ¿Qué tan grande es mi dataset? (filas, columnas)
- `df.head()` → ¿Cómo se ven las primeras filas?
- `df.info()` → ¿Hay valores nulos? ¿Qué tipo de datos tengo?
- `df.describe()` → ¿Cuál es el rango, la media, la desviación de cada variable?

### Paso 4: Filtrar datos
```python
# Vinos buenos (calidad >= 7)
vinos_buenos = df[df['quality'] >= 7]

# Vinos con alto alcohol Y bajo pH (filtrar con dos condiciones)
vinos_selectos = df[(df['alcohol'] >= 11.0) & (df['pH'] <= 3.3)]

# Vinos malos O buenos (filtrar con OR)
vinos_extremos = df[(df['quality'] <= 4) | (df['quality'] >= 7)]
```

### Paso 5: GroupBy
```python
# ¿Cuál es el promedio de alcohol por nivel de calidad?
df.groupby('quality')['alcohol'].mean()

# Múltiples estadísticas a la vez
df.groupby('quality').agg({
    'alcohol': ['mean', 'std', 'min', 'max'],
    'pH': ['mean', 'std']
})
```

### Paso 6: Visualizar
Creamos 5 gráficos que cuentan historias diferentes sobre los datos:
1. **Distribución de calidad** — ¿Hay muchos vinos buenos?
2. **Alcohol vs Calidad** — ¿Los vinos con más alcohol son mejores?
3. **Matriz de correlación** — ¿Qué variables se relacionan?
4. **Pairplot** — ¿Hay patrones visuales entre variables?
5. **Acidez volátil vs Calidad** — ¿La acidez daña la calidad?

---

## 📊 Resultados

### ¿Qué descubrimos sobre los vinos?

| Variable | Relación con calidad |
|----------|---------------------|
| Alcohol | ✅ **Positiva**: más alcohol = mejor calidad |
| Acidez volátil | ❌ **Negativa**: más acidez volátil = peor calidad |
| Ácido cítrico | ✅ **Positiva**: más ácido cítrico = mejor calidad |
| Sulfatos | ✅ **Positiva**: más sulfatos = mejor calidad |

### Visualizaciones generadas

| Archivo | Qué muestra |
|---------|-------------|
| `docs/distribucion_calidad.png` | Cuántos vinos hay en cada nivel de calidad |
| `docs/alcohol_vs_calidad.png` | Relación entre alcohol y calidad (boxplot) |
| `docs/matriz_correlacion.png` | Mapa de calor de correlaciones entre variables |
| `docs/pairplot_vino.png` | Relaciones por pares entre variables clave |
| `docs/acidez_vs_calidad.png` | Acidez volátil vs calidad (violin plot) |

---

## 💡 Conceptos clave

- **DataFrame**: Tabla bidimensional (filas y columnas) — la estructura principal de pandas
- **Filtrado**: Seleccionar filas que cumplen condiciones → `df[df['col'] > valor]`
- **groupby()**: Agrupar datos por una categoría y calcular estadísticas por grupo
- **Correlación**: Mide cómo se mueven dos variables juntas (-1 a +1)
- **Feature engineering**: Crear nuevas columnas a partir de las existentes para mejorar modelos
- **.agg()**: Aplicar múltiples funciones de agregación a la vez

---

## 🚀 Siguiente paso

Después de dominar estos fundamentos de pandas, el siguiente proyecto será:

**Proyecto 2 — numpy y Operaciones Vectorizadas**
Aprenderás a usar arrays de numpy para operaciones matemáticas rápidas, vectores, y preparar datos para algoritmos de ML. Es el complemento perfecto a pandas.
