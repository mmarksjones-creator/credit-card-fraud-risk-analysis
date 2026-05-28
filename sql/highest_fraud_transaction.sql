-- Find the highest fraudulent transaction amount
SELECT 
    MAX(Amount) AS highest_fraud_transaction
FROM "Credit card fraud Analysis"
WHERE Class = 1;
