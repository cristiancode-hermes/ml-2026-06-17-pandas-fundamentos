#!/usr/bin/env python3
"""
🍷 PROYECTO: Explorando la Calidad del Vino Tinto con pandas
=================================================================
Nivel 1 — Skill: pandas (DataFrames, CSV, filtros, groupby)

¿QUÉ VAS A APRENDER?
- Cargar un CSV real con pandas (¡los datos tienen ";" como separador!)
- Explorar un DataFrame: forma, columnas, tipos de datos
- Filtrar filas (vinos buenos, vinos baratos en alcohol)
- Agrupar con groupby() y calcular estadísticas por grupo
- Visualizar relaciones entre variables

DATOS REALES: Vinos tintos portugueses (Vinho Verde)
Fuente: UCI Machine Learning Repository — Wine Quality Dataset
https://archive.ics.uci.edu/ml/datasets/Wine+Quality
"""

# =====================================================================
# PASO 1: Importar las librerías
# =====================================================================
# pandas es la navaja suiza del ML para datos tabulares (tablas)
# numpy nos da operaciones matemáticas rápidas
# matplotlib y seaborn son para hacer gráficos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear carpeta para gráficos si no existe
os.makedirs('docs', exist_ok=True)

print("=" * 70)
print("🍷 BIENVENIDO A TU PRIMER PROYECTO DE ML CON DATOS REALES")
print("=" * 70)

# =====================================================================
# PASO 2: Cargar los datos
# =====================================================================
# El archivo usa ";" como separador (no coma) porque es un CSV europeo
# ¡Ojo! Si no le decimos sep=';', pandas leerá todo como una sola columna
print("\n📂 Cargando datos de vinos tintos portugueses...")
df = pd.read_csv('data/winequality-red.csv', sep=';')

# ---------------------------------------------------------------------
# ¿Qué acabamos de hacer?
# pd.read_csv() es la función MÁS IMPORTANTE de pandas para ML.
# Carga archivos CSV (Comma-Separated Values) en un DataFrame.
# Un DataFrame es como una hoja de Excel en Python: filas y columnas.
# ---------------------------------------------------------------------

# =====================================================================
# PASO 3: Primer vistazo a los datos — ¡siempre empezar aquí!
# =====================================================================
print("\n🔍 PRIMER VISTAZO A LOS DATOS")
print("-" * 50)

# .shape te da (filas, columnas) — como medir el tamaño de tu mesa de trabajo
print(f"📏 Dimensiones: {df.shape[0]} filas (vinos) x {df.shape[1]} columnas (características)")

# .head() muestra las primeras 5 filas — como abrir el archivo y ver el principio
print("\n👀 Primeras 5 filas (usa head() para no saturar la pantalla):")
print(df.head())

# .info() es tu mejor amiga: te dice tipos de datos y si hay valores nulos
print("\n📋 Info del DataFrame (tipos de datos y valores nulos):")
print(df.info())

# .describe() te da estadísticas básicas de cada columna numérica
# media, desviación estándar, mínimo, máximo, percentiles
print("\n📊 Estadísticas descriptivas (describe()):")
print(df.describe().round(2))

# ¿Cuántos vinos de cada calidad hay?
print("\n🏷️ Distribución de la calidad del vino (columna 'quality'):")
# quality va de 0 a 10, pero en este dataset va de 3 a 8
print(df['quality'].value_counts().sort_index())

# =====================================================================
# PASO 4: Limpieza básica — ¿hay datos faltantes?
# =====================================================================
print("\n🧹 VERIFICANDO DATOS FALTANTES")
print("-" * 50)
# isnull() + sum() te dice cuántos valores nulos hay por columna
# En ML, los datos nulos son un problema común que hay que resolver
nulos = df.isnull().sum()
print(f"Valores nulos por columna:\n{nulos}")
print(f"\n✅ ¡Buenas noticias! Total de nulos en todo el dataset: {nulos.sum()}")

# =====================================================================
# PASO 5: FILTRAR DATOS — como buscar en Excel pero con código
# =====================================================================
print("\n🔎 FILTRANDO DATOS — el superpoder de pandas")
print("-" * 50)

# ---- Filtro simple: vinos de calidad alta (quality >= 7) ----
# En ML, filtrar es esencial para quedarte solo con los datos que te interesan
vinos_buenos = df[df['quality'] >= 7]
print(f"🍷 Vinos de calidad alta (quality >= 7): {len(vinos_buenos)} de {len(df)}")
print(vinos_buenos[['alcohol', 'pH', 'quality']].head())

# ---- Filtro compuesto: vinos con ALTO alcohol Y bajo pH ----
# Usamos & (AND) para combinar condiciones. Cada condición va entre paréntesis.
# Esto es como decir: "dame los vinos que sean fuertes y ácidos"
vinos_selectos = df[(df['alcohol'] >= 11.0) & (df['pH'] <= 3.3)]
print(f"\n🥇 Vinos con alcohol>=11% y pH<=3.3: {len(vinos_selectos)} vinos")
print(vinos_selectos[['alcohol', 'pH', 'quality']].head())

# ---- Filtro con OR: vinos muy malos O muy buenos ----
# Usamos | (OR) para alternativas: "o son malos o son buenos, los regulares no"
# quality <= 4 son vinos malos, quality >= 7 son buenos
vinos_extremos = df[(df['quality'] <= 4) | (df['quality'] >= 7)]
print(f"\n⚡ Vinos extremos (quality<=4 o quality>=7): {len(vinos_extremos)} vinos")
print(f"   - Malos (<=4): {len(df[df['quality']<=4])}")
print(f"   - Buenos (>=7): {len(df[df['quality']>=7])}")

# ---- Usando .query() — una forma más legible de filtrar ----
# .query() te permite escribir la condición como texto, sin paréntesis raros
print("\n📝 Usando .query() para filtrar (más legible):")
vinos_ligeros = df.query('alcohol < 10.0 and quality > 5')
print(f"Vinos ligeros (alcohol<10%) con calidad>5: {len(vinos_ligeros)} vinos")
print(vinos_ligeros[['alcohol', 'quality', 'residual sugar']].head())

# =====================================================================
# PASO 6: GROUPBY — el rey del análisis agregado
# =====================================================================
print("\n📊 GROUPBY — AGRUPANDO Y ANALIZANDO POR CATEGORÍAS")
print("-" * 50)

# ---- groupby básico: promedio de cada variable por nivel de calidad ----
# groupby() es como la función "Tabla Dinámica" de Excel, pero mucho más poderosa
# Agrupamos por 'quality' y calculamos el promedio de todo
print("\n📈 Características promedio por nivel de calidad:")
promedio_por_calidad = df.groupby('quality').mean().round(2)
print(promedio_por_calidad)

# ---- ¿El alcohol se relaciona con la calidad? ----
# Los vinos mejor calificados suelen tener más alcohol (observación del mundo real)
print("\n🍷 Alcohol promedio por nivel de calidad:")
alcohol_por_calidad = df.groupby('quality')['alcohol'].mean().round(2)
print(alcohol_por_calidad)

# ---- Varias estadísticas a la vez con .agg() ----
# .agg() te permite calcular diferentes funciones para diferentes columnas
# Es como: "dame el promedio del alcohol, la mediana del pH y el máximo de azúcar"
print("\n📊 Estadísticas múltiples con .agg():")
stats = df.groupby('quality').agg({
    'alcohol': ['mean', 'std', 'min', 'max'],
    'pH': ['mean', 'std'],
    'residual sugar': 'max',
    'volatile acidity': 'mean'
}).round(2)
print(stats)

# ---- Contar cuántos vinos hay en cada categoría de calidad ----
# .size() te da el conteo de elementos en cada grupo
print("\n📋 Conteo de vinos por nivel de calidad:")
conteo_calidad = df.groupby('quality').size()
print(conteo_calidad)

# ---- Groupby con múltiples columnas ----
# Podemos agrupar por combinaciones de columnas
# Creamos una categoría de "acidez" basada en pH
# Esto se llama "feature engineering" — crear nuevas columnas a partir de las existentes

# Crear una columna categórica de nivel de acidez
# .cut() divide los valores en intervalos (bins) y les asigna etiquetas
df['acidity_level'] = pd.cut(
    df['pH'],
    bins=[2.5, 3.0, 3.3, 3.6, 4.5],
    labels=['Muy ácido', 'Ácido', 'Moderado', 'Poco ácido']
)

print("\n🏷️ Distribución por nivel de acidez (nueva columna creada):")
print(df['acidity_level'].value_counts())

# Groupby doble: calidad y nivel de acidez
print("\n📊 Alcohol promedio por calidad y nivel de acidez:")
grupos_dobles = df.groupby(['quality', 'acidity_level'])['alcohol'].mean().round(2)
print(grupos_dobles)

# =====================================================================
# PASO 7: VISUALIZACIONES — un gráfico vale más que mil tablas
# =====================================================================
print("\n📈 CREANDO VISUALIZACIONES...")
print("-" * 50)

# ---- Gráfico 1: Distribución de la calidad del vino ----
# Un countplot muestra cuántos vinos hay en cada nivel de calidad
# Es el primer gráfico que debes hacer para entender tu variable objetivo
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='quality', hue='quality', palette='RdYlGn', legend=False)
plt.title('Distribución de la Calidad del Vino Tinto', fontsize=15, fontweight='bold')
plt.xlabel('Calificación (0-10)', fontsize=12)
plt.ylabel('Cantidad de vinos', fontsize=12)
# Añadir etiquetas con los valores exactos sobre cada barra
for i, v in enumerate(df['quality'].value_counts().sort_index().values):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('docs/distribucion_calidad.png', dpi=100)
print("   ✅ Guardado: docs/distribucion_calidad.png")
plt.close()

# ---- Gráfico 2: Alcohol vs Calidad (boxplot) ----
# Un boxplot muestra la distribución del alcohol para cada nivel de calidad
# Los boxplots son GENIALES para ver diferencias entre grupos
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='quality', y='alcohol', hue='quality', palette='RdYlGn', legend=False)
plt.title('¿A más alcohol, mejor calidad?', fontsize=15, fontweight='bold')
plt.xlabel('Calidad', fontsize=12)
plt.ylabel('% Alcohol', fontsize=12)
# Línea punteada con el promedio general de alcohol
promedio_alcohol = df['alcohol'].mean()
plt.axhline(y=promedio_alcohol, color='red', linestyle='--', alpha=0.7,
            label=f'Promedio general: {promedio_alcohol:.2f}%')
plt.legend()
plt.tight_layout()
plt.savefig('docs/alcohol_vs_calidad.png', dpi=100)
print("   ✅ Guardado: docs/alcohol_vs_calidad.png")
plt.close()

# ---- Gráfico 3: Matriz de correlación (heatmap) ----
# La correlación mide cómo se relacionan las variables entre sí
# Valores cerca de +1: suben juntos | cerca de -1: uno sube, el otro baja
# Usamos SOLO columnas numéricas para la correlación
cols_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
# Excluimos 'quality' porque la queremos como referencia, no como variable a predecir aún
cols_numericas.remove('quality')

plt.figure(figsize=(14, 10))
correlacion = df[cols_numericas + ['quality']].corr()
sns.heatmap(correlacion, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', linewidths=1, square=True)
plt.title('Matriz de Correlación — ¿Qué variables se relacionan con la calidad?',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('docs/matriz_correlacion.png', dpi=100)
print("   ✅ Guardado: docs/matriz_correlacion.png")
plt.close()

# ---- Gráfico 4: Pairplot (solo algunas columnas para no saturar) ----
# El pairplot muestra la relación entre pares de variables
# Es útil para detectar patrones visualmente, pero con muchas columnas es lento
columnas_para_plot = ['alcohol', 'volatile acidity', 'citric acid', 'quality']
# Convertimos quality a string para que seaborn la trate como categoría
df_plot = df.copy()
df_plot['quality'] = df_plot['quality'].astype(str)

plt.figure(figsize=(12, 10))
sns.pairplot(data=df_plot, vars=columnas_para_plot[:-1], hue='quality',
             palette='RdYlGn', diag_kind='kde')
plt.suptitle('Relaciones entre variables químicas del vino', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('docs/pairplot_vino.png', dpi=100)
print("   ✅ Guardado: docs/pairplot_vino.png")
plt.close()

# ---- Gráfico 5: Acidez volátil vs Calidad ----
# La acidez volátil es una de las variables que más se correlaciona (negativamente)
# con la calidad del vino. A más acidez volátil, peor vino.
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='quality', y='volatile acidity', hue='quality', palette='RdYlGn', legend=False)
plt.title('Acidez Volátil por Nivel de Calidad', fontsize=15, fontweight='bold')
plt.xlabel('Calidad', fontsize=12)
plt.ylabel('Acidez Volátil (g/dm³)', fontsize=12)
plt.axhline(y=df['volatile acidity'].mean(), color='red', linestyle='--',
            alpha=0.7, label=f'Promedio: {df["volatile acidity"].mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig('docs/acidez_vs_calidad.png', dpi=100)
print("   ✅ Guardado: docs/acidez_vs_calidad.png")
plt.close()

# =====================================================================
# PASO 8: OPERACIONES ADICIONALES CON PANDAS
# =====================================================================
print("\n🛠️  MÁS OPERACIONES ÚTILES DE PANDAS")
print("-" * 50)

# ---- Ordenar datos ----
# .sort_values() ordena el DataFrame por una columna
print("\n⬆️  Top 5 vinos con más alcohol:")
print(df.sort_values('alcohol', ascending=False)[['alcohol', 'quality', 'pH']].head())

# ---- Seleccionar columnas específicas ----
# Puedes seleccionar columnas como si fueran llaves de un diccionario
columnas_interes = ['alcohol', 'pH', 'sulphates', 'quality']
print(f"\n📌 Columnas seleccionadas: {columnas_interes}")
print(df[columnas_interes].head())

# ---- Renombrar columnas ----
# .rename() es útil para dar nombres más claros
df_renombrado = df.rename(columns={
    'volatile acidity': 'acidez_volatil',
    'citric acid': 'acido_citrico',
    'residual sugar': 'azucar_residual'
})
print(f"\n✏️  Columnas renombradas: {list(df_renombrado.columns[:5])}")

# ---- Crear nuevas columnas derivadas ----
# Esto es feature engineering: crear predictores a partir de los existentes
df['ratio_alcohol_acidez'] = df['alcohol'] / df['pH']
df['sulfatos_por_alcohol'] = df['sulphates'] / df['alcohol']
print("\n🧪 Nuevas columnas creadas (feature engineering):")
print(f"   - ratio_alcohol_acidez (alcohol / pH)")
print(f"   - sulfatos_por_alcohol (sulphates / alcohol)")
print(df[['alcohol', 'pH', 'ratio_alcohol_acidez']].head())

# ---- Muestreo aleatorio ----
# sample() toma una muestra aleatoria de filas — útil para inspeccionar datos grandes
print("\n🎲 Muestra aleatoria de 5 vinos:")
print(df[['alcohol', 'quality', 'pH']].sample(5, random_state=42))

# ---- Los 3 mejores vinos por cada nivel de calidad ----
print("\n🥇 Top 3 vinos con más alcohol por cada nivel de calidad:")
# Otra forma: ordenamos todo y luego agrupamos
top_por_calidad = (
    df.sort_values('alcohol', ascending=False)
    .groupby('quality')
    .head(3)
    .sort_values(['quality', 'alcohol'], ascending=[True, False])
    [['quality', 'alcohol', 'pH']]
)
print(top_por_calidad)

# =====================================================================
# 🧠 RESUMEN FINAL — ¿Qué aprendiste hoy?
# =====================================================================
print("\n" + "=" * 70)
print("🧠 RESUMEN: HOY APRENDISTE...")
print("=" * 70)

# Calculamos los valores antes para usarlos en el resumen
alcohol_buenos = df[df['quality'] >= 7]['alcohol'].mean()
alcohol_malos = df[df['quality'] <= 4]['alcohol'].mean()

print(f"""
✅ 1. CARGAR DATOS REALES con pd.read_csv() y separador personalizado (sep=';')
✅ 2. EXPLORAR un DataFrame con head(), info(), describe(), shape
✅ 3. FILTRAR datos con condiciones: df[df['columna'] > valor]
✅ 4. COMBINAR filtros con & (AND) y | (OR)
✅ 5. AGRUPAR con groupby() y calcular estadísticas por grupo
✅ 6. CREAR visualizaciones: countplot, boxplot, heatmap, pairplot
✅ 7. HACER feature engineering básico creando nuevas columnas
✅ 8. USAR .query(), .sort_values(), .sample(), .rename()

🔑 CONCEPTO CLAVE DEL DÍA:
   Pandas es la HERRAMIENTA #1 para trabajar con datos tabulares en ML.
   Todo proyecto de ML empieza con: "import pandas as pd"
   Y termina con: "¿Qué me dicen los datos?"

📊 DATO CURIOSO DEL DATASET:
   El alcohol promedio de los vinos de calidad >= 7 es {alcohol_buenos:.1f}%
   vs {alcohol_malos:.1f}% para los de calidad <= 4.
   ¡El alcohol SÍ importa para la calidad!
""")
