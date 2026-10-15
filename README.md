# AWS Retail Batch Data Pipeline

## Project Overview

A retail analytics project that processes sales data using Amazon S3, Python, Apache Airflow, and Amazon Athena.

The pipeline reads raw CSV data from S3, validates and transforms sales records, and writes cleaned data in compressed Parquet format. Airflow schedules the processing workflow, while Athena SQL queries support revenue analysis.

## Architecture

**S3 Raw CSV → Python ETL scheduled by Airflow → S3 Parquet → Athena SQL**

Airflow can run on an EC2 instance. Tableau can be connected to Athena as a future visualization enhancement.

## Data Lake Organization

| Layer | Example S3 location | Purpose |
|---|---|---|
| Raw | `s3://YOUR_BUCKET/raw/csv/OnlineRetail.csv` | Source retail transactions |
| Clean | `s3://YOUR_BUCKET/clean/online_retail/online_retail_clean.parquet` | Validated sales records |
| Query results | Configure in Athena | Store SQL query results |

The bucket name and object paths are configurable.

## Technologies Used

- **Amazon S3:** Raw and cleaned data storage.
- **Python and pandas:** Data validation and transformation.
- **PyArrow:** Snappy-compressed Parquet output.
- **Apache Airflow:** Daily scheduling, task retries, and execution timeout.
- **Amazon Athena:** SQL analysis of cleaned retail data.
- **AWS IAM:** Role-based access configured during deployment.
- **S3 server-side encryption:** S3-managed encryption or optional AWS KMS encryption for output.
- **Git and GitHub:** Source control and project documentation.

## Pipeline Workflow

1. Upload the source retail CSV to the S3 raw layer.
2. Trigger the ETL manually or through the scheduled Airflow DAG.
3. Validate that all required source columns are present.
4. Exclude cancelled invoices, invalid dates, invalid customer IDs, and nonpositive quantities or prices.
5. Calculate sales value as quantity multiplied by unit price.
6. Extract year and month for time-based analysis.
7. Write cleaned records to S3 as compressed Parquet with explicit server-side encryption.
8. Log input, output, and rejected record counts.
9. Run Athena queries to analyze the cleaned dataset.

## Analytics Supported

- Total positive sales revenue.
- Top countries by sales revenue.
- Monthly sales trends.

Cancelled orders and returns are excluded, so these results represent positive sales rather than net revenue after returns.

## Reliability and Security

- Configuration through environment variables.
- No hardcoded AWS credentials.
- Schema validation before processing.
- Failure before upload when no valid records remain.
- Airflow retries and task execution timeout.
- A consistent output key to prevent duplicate files during reruns.
- Configurable S3-managed or KMS-based output encryption.

Bucket policies, IAM permissions, raw-file encryption, and Athena query-result encryption must be configured separately during deployment.

## Testing

Five local tests cover transformation results, required columns, empty valid output, nonfinite numeric values, and encryption configuration.

AWS and Airflow deployment still require validation in the target environment.

## Current Scope

The project performs a full refresh and processes data in memory using pandas. Athena queries are provided separately from the Airflow workflow.

## Future Enhancements

- Incremental ingestion and historical processing.
- Parquet partitioning by year and month.
- A quarantine layer for rejected records.
- Automated Athena query execution.
- Monitoring and failure notifications.
- Infrastructure as code and CI checks.
- A Tableau dashboard.

## Project Provenance

This project adapts an existing retail pipeline baseline with additional configuration, validation, encryption options, tests, and documentation. Included reference screenshots show the original baseline; updated deployment screenshots should be captured after running this version.
