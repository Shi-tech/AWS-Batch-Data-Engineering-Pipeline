-- ============================================
-- Athena Analytics Queries
-- Dataset: Online Retail (Clean Layer)
-- Table: online_retail_clean
-- ============================================

-- ------------------------------------------------
-- 1. Total Revenue
-- ------------------------------------------------
SELECT
    ROUND(SUM(total_price), 2) AS total_revenue
FROM online_retail_clean;

-- ------------------------------------------------
-- 2. Top 10 Countries by Revenue
-- ------------------------------------------------
SELECT
    country,
    ROUND(SUM(total_price), 2) AS revenue
FROM online_retail_clean
GROUP BY country
ORDER BY revenue DESC
LIMIT 10;

-- ------------------------------------------------
-- 3. Monthly Revenue Trend
-- ------------------------------------------------
SELECT
    year,
    month,
    ROUND(SUM(total_price), 2) AS monthly_revenue
FROM online_retail_clean
GROUP BY year, month
ORDER BY year, month;
