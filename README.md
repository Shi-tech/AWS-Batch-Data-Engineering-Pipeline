# AWS Batch Data Engineering Pipeline (End-to-End)

## Project Overview
This project demonstrates a real-world, end-to-end batch data engineering pipeline built on AWS.

The pipeline ingests raw CSV data into an Amazon S3 data lake, performs data cleaning and transformations using Python, orchestrates workflows using Apache Airflow running on EC2, enables analytics using Amazon Athena, and supports downstream visualization using BI tools such as Tableau.

This project closely mirrors industry-grade data engineering practices, including layered data lakes, batch orchestration, schema optimization, and analytics-ready data modeling.

---

## Architecture Overview

### Data Flow

Raw CSV (Amazon S3)  
↓  
Apache Airflow (EC2)  
↓  
Python ETL (pandas)  
↓  
S3 Clean Layer (Parquet)  
↓  
Amazon Athena (SQL Analytics)  
↓  
Visualization (Tableau)

---

## Data Lake Structure

s3://de-batch-data-lake-prakash/  
│  
├── raw/  
│   └── csv/  
│       └── OnlineRetail.csv  
│  
├── clean/  
│   └── online_retail/  
│       └── online_retail_clean.parquet  
│  
└── analytics/
│   └── final

---

## Technologies Used

- Amazon S3 – Data lake storage (raw and clean layers)
- Apache Airflow – Workflow orchestration (running on EC2)
- Python (pandas) – Data cleaning and transformations
- Amazon Athena – Serverless SQL analytics
- AWS IAM – Secure role-based access control
- Tableau – Data visualization and dashboards
- GitHub – Version control and documentation

---

## Pipeline Workflow

1. Raw retail CSV data is uploaded to Amazon S3 (raw layer)
2. An Apache Airflow DAG orchestrates the batch workflow
3. Python ETL script performs:
   - Removal of invalid and null records
   - Data type normalization
   - Revenue calculation (quantity × unit_price)
   - Date enrichment (year, month)
4. Cleaned data is written back to S3 in Parquet format
5. Amazon Athena is used to query analytics-ready data
6. Aggregated insights are visualized using Tableau

---

## Key Insights Generated

- Overall business revenue
- Top revenue-generating countries
- Monthly revenue trends
- Optimized analytics using Parquet format

---

## What I Learned

- Designing S3-based data lake architectures
- Building and operating Apache Airflow on EC2
- Writing production-style Python ETL pipelines
- Managing secure AWS access using IAM roles
- Query optimization using Parquet and Athena
- Understanding batch processing cost considerations

---

## Future Enhancements

- Partition Parquet data by year and month
- Add data quality checks in Airflow
- Automate scheduling and monitoring
- Enable BI auto-refresh
- Add alerting and logging

---

## Why This Project Matters

This project reflects how modern batch data engineering pipelines are implemented in production, combining cloud storage, orchestration, transformation, analytics, and visualization into a scalable and maintainable system.
