-- Count total fraudulent transactions
SELECT 
    COUNT(*) AS fraud_transactions
FROM "Credit card fraud Analysis"
WHERE Class = 1;
