# Credit Card Fraud Detection & Risk Analysis

**Tools:** Excel · SQL · Python · Power BI

Financial fraud is difficult to detect in large transaction datasets because fraudulent activity is rare, inconsistent, and easy to miss without a structured analysis workflow. This project analyzes 284,807 real credit card transactions to identify fraud patterns, validate risk KPIs across four tools, and deliver actionable recommendations for reducing exposure.

**Bottom line:** 492 fraudulent transactions out of 284,807 represent a 0.173% fraud rate — but those transactions account for ~$60,127 in total exposure, with activity spiking sharply around hours 8 and 41.

---

## Dashboard previews

### Power BI dashboard
![Power BI Dashboard](Fraud%20Power%20BI%20Dashboard.png)

### Power BI dashboard — active filters
![Power BI Dashboard Active](Fraud%20Power%20BI%20Dashboard%20Active%20.png)

### Excel dashboard
![Excel Dashboard](Excel%20Fraud%20Dashboard.png)

### Raw data view
![Raw Data](Raw%20credit%20card%20fraud%20data%20excel.png)

---

## Key findings

| Metric | Result |
|---|---|
| Total transactions analyzed | 284,807 |
| Fraudulent transactions | 492 |
| Fraud rate | 0.173% |
| Total fraud exposure | ~$60,127.97 |
| Average fraud amount | ~$122.21 |
| Highest single fraud transaction | See dashboard |
| Peak fraud hours | Hours 8 and 41 |

---

## Business recommendations

1. Implement enhanced fraud alert monitoring during hours 8 and 41 — these periods showed statistically significant spikes in fraudulent activity
2. Flag transactions above the average fraud amount ($122.21) for additional verification, particularly during peak hours
3. Apply anomaly detection rules to the 0–1% transaction range where fraud is concentrated — a tiered alert system would catch the majority of exposure without flagging legitimate transactions
4. Cross-reference high-value transactions against time-of-day risk scores before processing

---

## Project workflow

1. Loaded and cleaned the 284,807-row dataset in Excel — standardized columns, removed formatting issues, prepared for analysis
2. Built PivotTables and KPI cards in Excel to summarize fraud count, fraud rate, exposure, and hourly trends
3. Wrote SQL queries to independently calculate every KPI: fraud count, fraud rate, total exposure, average fraud amount, highest transaction, and fraud by hour
4. Used Python/Pandas to automate KPI validation and confirm all figures matched across tools
5. Rebuilt the full analysis in Power BI with DAX measures, slicers, KPI cards, and drill-down visuals

---

## Project structure

```
├── sql/                              # SQL queries for all KPI calculations
├── visuals/                          # Additional visual assets
├── fraud_kpi_validation.py           # Python validation script
├── Credit card sample data.xlsx      # Sample dataset (full file exceeds GitHub limits)
├── Excel Fraud Dashboard.png         # Excel dashboard screenshot
├── Fraud Power BI Dashboard.png      # Power BI dashboard screenshot
├── Fraud Power BI Dashboard Active.png  # Power BI with active slicer filters
├── Raw credit card fraud data excel.png # Raw data view
└── fraud_project_overview.png        # Project summary visual
```

---

## How to explore this project

- Browse the `sql/` folder to see all KPI queries used in the analysis
- Open `fraud_kpi_validation.py` to see the Python validation workflow
- View dashboard screenshots above — Power BI and Excel dashboards are both included
- Full 284K-row dataset not included due to GitHub size limits; available on request
- Power Bi Dashboard link(https://app.powerbi.com/links/qWU690UCks?ctid=7cf1d100-35b0-4cec-a70d-9b8bd80b9ad0&pbi_source=linkShare)

---

## About

Built by **M'Khi A. Marksjones** — MIS student at Angelo State University, Dean's List Spring 2026.  
Seeking entry-level analyst roles in Texas (Financial Analyst I, Reporting Analyst, Business Analyst, Data Analyst).

[LinkedIn](https://www.linkedin.com/in/m-khi-marksjones-447607396) · [GitHub](https://github.com/mmarksjones-creator)

