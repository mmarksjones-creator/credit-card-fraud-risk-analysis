-- Calculate total dollar amount lost to fraudulent transactions
SELECT 
    ROUND(SUM(Amount), 2) AS total_fraud_loss
FROM "Credit card fraud Analysis"
WHERE Class = 1;
