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

SELECT new_cars.brand,
	new_cars.model,
	new_cars.fuel_type,
	new_cars.new_price,
	used_cars.used_price, 
 ROUND(((new_cars.new_price - used_cars.used_price) / new_cars.new_price) * 100, 2) AS drop_percent
FROM new_cars
INNER JOIN used_cars ON new_cars.brand = used_cars.brand 
	AND new_cars.model = used_cars.model
	AND new_cars.fuel_type = used_cars.fuel_type
ORDER BY drop_percent DESC
