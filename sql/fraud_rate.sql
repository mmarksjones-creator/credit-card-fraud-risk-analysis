-- Calculate fraud rate as a percentage of all transactions
SELECT 
    ROUND((SUM(Class) * 100.0 / COUNT(*)), 3) AS fraud_rate_percent
FROM "Credit card fraud Analysis";
