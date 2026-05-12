WITH new_cars AS (SELECT 
    brand, 
    model, 
    fuel_type, 
    ROUND(AVG(price)) AS new_price
FROM clean_cars
WHERE year >= 2022 AND fuel_type IN ('electric', 'gasoline')
GROUP BY brand, model, fuel_type),

used_cars AS (
SELECT
	brand, 
    model, 
    fuel_type, 
    ROUND(AVG(price)) AS used_price
FROM clean_cars
WHERE year = 2018 AND fuel_type IN ('electric', 'gasoline')
GROUP BY brand,model, fuel_type
)

SELECT 
    u.brand, 
    u.model, 
    u.fuel_type, 
    ((n.new_price - u.price) / n.new_price) * 100 as drop_percent
FROM new_cars n
JOIN clean_cars u ON n.brand = u.brand AND n.model = u.model AND n.fuel_type = u.fuel_type
WHERE u.year = 2018;
