--Transformaciones y Limpieza

---¿Cómo fusionarías los tres DataFrames/tablas en uno solo?

SELECT 
    s.Store,
    s.Dept,
    s.Date,
    s.Weekly_Sales,
    s.IsHoliday AS SaleHoliday,
    
    f.Temperature,
    f.Fuel_Price,
    f.MarkDown1,
    f.MarkDown2,
    f.MarkDown3,
    f.MarkDown4,
    f.MarkDown5,
    f.CPI,
    f.Unemployment,
    f.IsHoliday AS FeatureHoliday,
    
    t.Type,
    t.Size
FROM [sales data-set] AS s
LEFT JOIN [Features data set] AS f
    ON s.Store = f.Store AND s.Date = f.Date
LEFT JOIN [stores data-set] AS t
    ON s.Store = t.Store;

---¿Qué tienda tuvo la mayor caída semana a semana? (delta negativo más grande)


SELECT 
    s.Store,
    t.Type,
    t.Size,
    AVG(TRY_CAST(f.Fuel_Price AS FLOAT)) AS Promedio_Fuel_Price
FROM [sales data-set] AS s
LEFT JOIN [Features data set] AS f
    ON s.Store = f.Store AND s.Date = f.Date
LEFT JOIN [stores data-set] AS t
    ON s.Store = t.Store
GROUP BY s.Store, t.Type, t.Size
HAVING AVG(TRY_CAST(f.Fuel_Price AS FLOAT)) > 3;


