import pandas as pd
# M'Khi Marksjones
df = pd.read_csv(r"C:\Users\Mkhi1\OneDrive\Documents\Credit card fraud Analysis.csv")

# Filter fraud transactions
fraud_df = df[df["Class"] == 1]

# KPI calculations
total_transactions = len(df)
fraud_transactions = len(fraud_df)
fraud_rate = (fraud_transactions / total_transactions) * 100
avg_fraud_amount = fraud_df["Amount"].mean()
total_fraud_loss = fraud_df["Amount"].sum()
highest_fraud_transaction = fraud_df["Amount"].max()

# Create hour column
df["Hour"] = (df["Time"] // 3600).astype(int)

# Fraud by hour summary
fraud_by_hour = (
    df[df["Class"] == 1]
    .groupby("Hour")
    .size()
)

# Print results
print("Financial Fraud Detection & Risk Analysis")
print("----------------------------------------")

print("Total Transactions:", total_transactions)
print("Fraud Transactions:", fraud_transactions)
print("Fraud Rate:", round(fraud_rate, 3), "%")
print("Average Fraud Amount: $", round(avg_fraud_amount, 2))
print("Total Fraud Loss: $", round(total_fraud_loss, 2))
print("Highest Fraud Transaction: $", round(highest_fraud_transaction, 2))

print("\nFraud Transactions by Hour:")
print(fraud_by_hour)

