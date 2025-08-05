<h1>🧠 Automatización ETL & Dashboard con Python, SQL y Power BI</h1>

<h2>🎯 Objetivo</h2>
<p>Automatizar el proceso completo de extracción, limpieza, análisis exploratorio y visualización de datos de ventas semanales utilizando Python, SQL y Power BI, con el fin de generar insights que permitan identificar tendencias, comportamientos atípicos y oportunidades de mejora en la toma de decisiones comerciales.</p>

<h2>⚙️ Tecnologías usadas</h2>
<ol>
<li>Python (Pandas, Matplotlib, etc.)</li>
<li>SQL Server / PostgreSQL</li>
<li>Power BI</li>
<li>Excel</li>
</ol>

<h2>🛠️ Pipeline del Proyecto</h2>

<ol >
<li>Exploración de Datos (EDA)</li>
<p>Realizada con Python</p>
<ul>Estadísticas descriptivas (media, mediana, desviación estándar) de las ventas.</ul>
<ul>Detección de outliers por tienda / departamento.</ul>
<ul>Relación visual entre el precio del combustible y las ventas.</ul>
<ul>Distribución general de los datos.</ul>

<li>Transformaciones y Limpieza</li>
<p>Con Python & SQL</p>
<ul>¿Cómo fusionarías los tres DataFrames/tablas en uno solo?</ul>
<ul>¿Qué tienda tuvo la mayor caída semana a semana? (delta negativo más grande)</ul>

<li>Análisis Avanzado</li>
<p>Cruzando diferentes fuentes de datos</p>
<ul>¿Cómo unirías las tablas para analizar ventas según tipo y tamaño de tienda?</ul>
<ul>¿Qué tiendas tuvieron un precio de combustible promedio mayor a 3 durante el año?</ul>

<li>Visualización con Power BI</li>

<ul>Evolución de ventas mensuales (incluyendo al menos 1 función DAX).</ul>
<ul>Comparación de ventas por tipo de tienda y por tamaño.</ul>

</ol>

<h2>📈 Resultados principales</h2>

<ol>
<li>
Se observa una tendencia estacional en las ventas, con picos pronunciados en los meses de diciembre de los años 2010 y 2012, lo cual se evidencia claramente en el gráfico de líneas mensual en Power BI.
</li>

<li>
El dashboard (gráfico circular) permite visualizar que las tiendas tipo A grandes concentran más del 64 % de las ventas totales, mientras que las tiendas de tipo C apenas superan el 6 %, lo cual indica una marcada dependencia del negocio hacia ciertos formatos.
</li>

<li>
El dashboard (gráfico de barras) permite visualizar que las ventas total e las tiendas de tamaño grande son 4.2 mil millones en unidades monetarias, mientras que las tiendas de tipo C apenas recauda 0.6 mil millones de unidades monetarias.
</li>
</ol>

<h2>🚀 Ejecución</h2>
<p>Cómo reproducir el proyecto paso a paso.</p>
<ol>
<li>Se debe descargar la data de Kaggle. El link es el siguiente: https://www.kaggle.com/datasets/manjeetsingh/retaildataset </li>
<li>Mediante python se hace el preprocesamiento de la data</li>
<li>Se une las 3 datas se realiza mediante python</li>
<li>Se conecta a Power BI para la generación de dashboard</li>
</ol>
