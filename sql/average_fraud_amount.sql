-- Calculate average fraudulent transaction amount
SELECT 
    ROUND(AVG(Amount), 2) AS avg_fraud_amount
FROM "Credit card fraud Analysis"
WHERE Class = 1;
