import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_stores = pd.read_csv("stores data-set.csv")
df_features = pd.read_csv("Features data set.csv")
df_sales = pd.read_csv("sales data-set.csv")

df_sales["Date"] = pd.to_datetime(df_sales["Date"], dayfirst=True)
df_features["Date"] = pd.to_datetime(df_features["Date"], dayfirst=True)

print("\n GENERAL PARTE 1")

print("\n tabla df_stores")
print(df_stores.isnull().sum())
print("\n tabla df_features")
print(df_features.isnull().sum())
print("\n tabla df_sales")
print(df_sales.isnull().sum())


print("\n Se identificaron valores nulos en las columnas MarkDown1 a MarkDown5 de la tabla Features, donde cada una presenta más del 60% de datos faltantes.")
print("Esto sugiere que muchas semanas no se realizaron promociones o que no se registraron correctamente.") 
print("En contraste, columnas como Temperature, Fuel_Price, CPI y Unemployment no presentan valores nulos o presentan muy pocos, lo que permite un análisis confiable de factores externos.")
print("El principal impacto de los nulos en las columnas de promoción es que pueden distorsionar el análisis de la influencia de descuentos sobre las ventas si no se tratan adecuadamente.")

print("\n GENERAL PARTE 2")

media = df_sales["Weekly_Sales"].mean()
mediana = df_sales["Weekly_Sales"].median()
desviacion = df_sales["Weekly_Sales"].std()
minimo = df_sales["Weekly_Sales"].min()
maximo = df_sales["Weekly_Sales"].max()
cantidad = df_sales["Weekly_Sales"].count()

print("\n Media:", media)
print("\n Mediana:", mediana)
print("\n Desviación estándar:", desviacion)
print("\n Mínimo:", minimo)
print("\n Máximo:", maximo)
print("\n Cantidad de registros:", cantidad)


print("\n GENERAL PARTE 3")

ventas_por_tienda = df_sales.groupby("Store")["Weekly_Sales"].sum().sort_values(ascending=False)
ventas_por_depto = df_sales.groupby("Dept")["Weekly_Sales"].sum().sort_values(ascending=False)

df_top_tiendas = ventas_por_tienda.head(3).reset_index().rename(columns={"Store": "Tienda", "Weekly_Sales": "Ventas Totales"})
df_bottom_tiendas = ventas_por_tienda.tail(3).reset_index().rename(columns={"Store": "Tienda", "Weekly_Sales": "Ventas Totales"})

df_top_deptos = ventas_por_depto.head(3).reset_index().rename(columns={"Dept": "Departamento", "Weekly_Sales": "Ventas Totales"})
df_bottom_deptos = ventas_por_depto.tail(3).reset_index().rename(columns={"Dept": "Departamento", "Weekly_Sales": "Ventas Totales"})

print("\n Tiendas con mayores ventas:")
print(df_top_tiendas)

print("\n Tiendas con menores ventas:")
print(df_bottom_tiendas)

print("\n Departamentos con mayores ventas:")
print(df_top_deptos)

print("\n Departamentos con menores ventas:")
print(df_bottom_deptos)

print("\nSe identificaron tiendas y departamentos con comportamientos atípicos en las ventas.")
print("Las tiendas con mayores ventas pueden corresponder a tiendas de mayor tamaño o con ubicación estratégica.")
print("Por otro lado, tiendas con ventas bajas pueden indicar bajo tráfico, menor tamaño o falta de promociones.")
print("Lo mismo aplica a departamentos: algunos tienen ventas consistentemente altas (posiblemente por alta demanda o promociones), mientras que otros tienen ventas muy bajas.")
print("Estos comportamientos deben considerarse como posibles outliers o patrones especiales en el análisis posterior.")


print("\n GENERAL PARTE 4")

df_comb = df_sales.merge(df_features[["Store", "Date", "Fuel_Price"]], on=["Store", "Date"], how="left")

df_comb = df_comb.dropna(subset=["Fuel_Price", "Weekly_Sales"])

corr = df_comb.corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, cmap='RdYlGn')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_comb, x="Fuel_Price", y="Weekly_Sales", alpha=0.3)
plt.title("Relación entre el precio del combustible y las ventas semanales")
plt.xlabel("Precio del Combustible")
plt.ylabel("Ventas Semanales")
plt.grid(True)
plt.tight_layout()
plt.show()

correlacion = df_comb["Fuel_Price"].corr(df_comb["Weekly_Sales"])
print(f"\nCorrelación entre Fuel_Price y Weekly_Sales: {correlacion:.4f}")

if correlacion > 0.2:
    interpretacion = "Existe una correlación positiva: cuando el precio del combustible sube, las ventas tienden a aumentar."
elif correlacion < -0.2:
    interpretacion = "Existe una correlación negativa: cuando el precio del combustible sube, las ventas tienden a disminuir."
else:
    interpretacion = "La correlación es débil o nula, lo que sugiere que el precio del combustible no afecta directamente las ventas semanales."

print("Interpretación:", interpretacion)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_comb, x="Date", y="Fuel_Price", alpha=0.3)
plt.title("Relación entre el precio del combustible y las semanas analizadas")
plt.xlabel("Semanas analizadas")
plt.ylabel("Precio del Combustible")
plt.grid(True)
plt.tight_layout()
plt.show()

df_comb["Date_num"] = df_comb["Date"].map(lambda x: x.toordinal())

correlacion = df_comb["Fuel_Price"].corr(df_comb["Date_num"])
print(f"\nCorrelación entre Fuel_Price y Date: {correlacion:.4f}")

if correlacion > 0.2:
    interpretacion = "Existe una correlación positiva: el precio del combustible ha aumentado con el tiempo."
elif correlacion < -0.2:
    interpretacion = "Existe una correlación negativa: el precio del combustible ha disminuido con el tiempo."
else:
    interpretacion = "No hay una tendencia clara en la evolución del precio del combustible a lo largo del tiempo."

print("Interpretación:", interpretacion)


print("\n En conclusión:")
print("\n La variable Fuel_price esta correlacionada con la variable Date, mas no con la variable Weekly_Sales")


print("\n GENERAL PARTE 5")


import matplotlib.pyplot as plt
import seaborn as sns

df_comb1 = df_sales.merge(
    df_features[["Store", "Date", "Fuel_Price", "Temperature", "CPI", "Unemployment"]],
    on=["Store", "Date"],
    how="left"
)

numericas = ["Weekly_Sales", "Fuel_Price", "Temperature", "CPI", "Unemployment"]

for col in numericas:
    plt.figure(figsize=(8, 5))
    sns.histplot(df_comb1[col], kde=True, bins=30, color='skyblue')
    plt.title(f"Distribución de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("\n La variable Weekly_Sales no cumple con la distribución normal.")
print("\n El sesgo es hacia la derecha o positivo. Esto indica que la mayor cantidad de ventas son inferiores y las mayores ventas son muy escasas.")
print("\n Además, hay presencia de Outliers.")


print("\n En el caso de la variable Fuel_Price, es un bimodal debido a que cuenta con dos picos altos.")
print("\n Tampoco es simetrico, por lo que no es una distribución normal.")

print("\n En el caso de la variable Temperature, tampoco corresponde a una distribución normal.")

print("\n Para la variable CPI tampoco cumple con la distribución normal.")

print("\n Para la variable Unemployment tampoco cumple con la distribución normal.")


for col in numericas:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df_comb1[col], color='salmon')
    plt.title(f"Detección de outliers en {col}")
    plt.xlabel(col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
print("\n Para la variable Weekly_Sales hay demasiados Outliers y coincide con el histograma.")

print("\n Para la variable Fuel_Price no presenta Outliers.")

print("\n Para la variable Temperature presenta 1 Outlier y está ubicado en el lado negativo.")

print("\n Para la variable CPI no presenta Outliers.")

print("\n Para la variable Unemployment presenta Outliers desde el 3 hasta el 4.4 y desde el 11.4 hasta el 14.5.")


print("\n")
print("\n PREGUNTA 2")

df_sales1 = pd.read_csv("sales data-set.csv")
df_features1 = pd.read_csv("Features data set.csv")
df_stores1 = pd.read_csv("stores data-set.csv")

df_sales1["Date"] = pd.to_datetime(df_sales1["Date"], dayfirst=True)
df_features1["Date"] = pd.to_datetime(df_features1["Date"], dayfirst=True)

df_merged1 = df_sales.merge(df_features, on=["Store", "Date"], how="left")

df_final = df_merged1.merge(df_stores, on="Store", how="left")
print("\n")
print(df_final.head(5))

print("\n")
print("\n PREGUNTA 3")

df_final_sorted = df_final.sort_values(by=["Store", "Dept", "Date"])

df_final_sorted["delta_ventas"] = df_final_sorted.groupby(["Store", "Dept"])["Weekly_Sales"].diff()

fila_caida_max = df_final_sorted.loc[df_final_sorted["delta_ventas"].idxmin()]

print("\n Tienda con la mayor caída de ventas semana a semana:")
print(f"Tienda: {int(fila_caida_max['Store'])}")
print(f"Departamento: {int(fila_caida_max['Dept'])}")
print(f"Caída en ventas: {fila_caida_max['delta_ventas']:.2f}")
print(f"Ventas esa semana: {fila_caida_max['Weekly_Sales']:.2f}")

