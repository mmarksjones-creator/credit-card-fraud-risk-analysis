-- Count fraudulent transactions by transaction hour
SELECT 
    FLOOR(Time / 3600) AS transaction_hour,
    COUNT(*) AS fraud_count
FROM "Credit card fraud Analysis"
WHERE Class = 1
GROUP BY transaction_hour
ORDER BY transaction_hour;
