"""
queries.py
==========

Computational Environmental Intelligence Framework (CEIF)

DuckDB SQL Query Library

Dataset
-------
environment_master

Responsibilities
----------------
1. Dataset Queries
2. Metadata Queries
3. AQI Analytics
4. PM Analytics
5. Weather Analytics
6. Trend Analysis
7. Station Analytics
8. Correlation Dataset
9. Forecast Dataset
"""

# ==========================================================
# DATASET
# ==========================================================

ENVIRONMENTAL_MASTER = """
SELECT *
FROM environmental_master
ORDER BY datetime;
"""

# ==========================================================
# METADATA
# ==========================================================

DATASET_INFO = """
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT station_id) AS total_stations,
    COUNT(DISTINCT district) AS total_districts,
    MIN(datetime) AS start_date,
    MAX(datetime) AS end_date
FROM environmental_master;
"""

STATION_LIST = """
SELECT DISTINCT
    station_id,
    station_name,
    district,
    latitude,
    longitude
FROM environmental_master
ORDER BY station_name;
"""

DISTRICT_LIST = """
SELECT DISTINCT
    district
FROM environmental_master
ORDER BY district;
"""

DATE_RANGE = """
SELECT

MIN(datetime) AS start_date,

MAX(datetime) AS end_date

FROM environmental_master;
"""

# ==========================================================
# AQI ANALYTICS
# ==========================================================

AVERAGE_AQI = """
SELECT

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master;
"""

MAXIMUM_AQI = """
SELECT

station_name,

district,

datetime,

aqi

FROM environmental_master

ORDER BY aqi DESC

LIMIT 10;
"""

MINIMUM_AQI = """
SELECT

station_name,

district,

datetime,

aqi

FROM environmental_master

ORDER BY aqi ASC

LIMIT 10;
"""

AQI_BY_STATION = """
SELECT

station_name,

district,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY

station_name,

district

ORDER BY average_aqi DESC;
"""

AQI_BY_DISTRICT = """
SELECT

district,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY district

ORDER BY average_aqi DESC;
"""

# ==========================================================
# DAILY AQI
# ==========================================================

DAILY_AQI = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

# ==========================================================
# MONTHLY AQI
# ==========================================================

MONTHLY_AQI = """
SELECT

YEAR(datetime) AS year,

MONTH(datetime) AS month,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY

year,

month

ORDER BY

year,

month;
"""

# ==========================================================
# YEARLY AQI
# ==========================================================

YEARLY_AQI = """
SELECT

YEAR(datetime) AS year,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY year

ORDER BY year;
"""

# ==========================================================
# HOURLY AQI
# ==========================================================

HOURLY_AQI = """
SELECT

HOUR(datetime) AS hour,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY hour

ORDER BY hour;
"""

# ==========================================================
# PM ANALYTICS
# ==========================================================

PM25_DAILY = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(pm25),2) AS average_pm25

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

PM10_DAILY = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(pm10),2) AS average_pm10

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

PM_SUMMARY = """
SELECT

ROUND(AVG(pm25),2) AS average_pm25,

ROUND(AVG(pm10),2) AS average_pm10,

MAX(pm25) AS maximum_pm25,

MAX(pm10) AS maximum_pm10

FROM environmental_master;
"""

# ==========================================================
# WEATHER ANALYTICS
# ==========================================================

WEATHER_SUMMARY = """
SELECT

ROUND(AVG(temperature),2) AS average_temperature,

ROUND(AVG(humidity),2) AS average_humidity,

ROUND(AVG(pressure),2) AS average_pressure,

ROUND(AVG(wind_speed),2) AS average_wind_speed,

ROUND(AVG(wind_gust),2) AS average_wind_gust

FROM environmental_master;
"""

TEMPERATURE_TREND = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(temperature),2) AS average_temperature

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

HUMIDITY_TREND = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(humidity),2) AS average_humidity

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

PRESSURE_TREND = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(pressure),2) AS average_pressure

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

WIND_SPEED_TREND = """
SELECT

DATE(datetime) AS date,

ROUND(AVG(wind_speed),2) AS average_wind_speed

FROM environmental_master

GROUP BY DATE(datetime)

ORDER BY date;
"""

# ==========================================================
# STATION ANALYTICS
# ==========================================================

STATION_RANKING = """
SELECT

station_name,

district,

ROUND(AVG(aqi),2) AS average_aqi,

ROUND(AVG(pm25),2) AS average_pm25,

ROUND(AVG(pm10),2) AS average_pm10

FROM environmental_master

GROUP BY

station_name,

district

ORDER BY average_aqi DESC;
"""

TOP_10_POLLUTED = """
SELECT *

FROM (

SELECT

station_name,

district,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY

station_name,

district

)

ORDER BY average_aqi DESC

LIMIT 10;
"""

TOP_10_CLEANEST = """
SELECT *

FROM (

SELECT

station_name,

district,

ROUND(AVG(aqi),2) AS average_aqi

FROM environmental_master

GROUP BY

station_name,

district

)

ORDER BY average_aqi ASC

LIMIT 10;
"""

# ==========================================================
# CORRELATION DATASET
# ==========================================================

CORRELATION_DATASET = """
SELECT

aqi,

pm25,

pm10,

temperature,

humidity,

pressure,

precipitation,

dew_point,

cloud_cover,

wind_speed,

wind_direction,

wind_gust

FROM environmental_master;
"""

# ==========================================================
# FORECAST DATASET
# ==========================================================

FORECAST_DATASET = """
SELECT *

FROM environmental_master

ORDER BY

station_id,

datetime;
"""

# ==========================================================
# MACHINE LEARNING DATASET
# ==========================================================

ML_DATASET = """
SELECT

station_id,

datetime,

aqi,

pm25,

pm10,

temperature,

humidity,

pressure,

precipitation,

dew_point,

cloud_cover,

wind_speed,

wind_direction,

wind_gust

FROM environmental_master

ORDER BY

station_id,

datetime;
"""