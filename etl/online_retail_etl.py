import pandas as pd
import boto3
from io import BytesIO


# Configuration

S3_BUCKET = "de-batch-data-lake-prakash"

RAW_KEY = "raw/csv/OnlineRetail.csv"
CLEAN_KEY = "clean/online_retail/online_retail_clean.parquet"

# Initialize S3 client
s3 = boto3.client("s3")


# Extract: Read CSV from S3
response = s3.get_object(Bucket=S3_BUCKET, Key=RAW_KEY)
df = pd.read_csv(response["Body"])


# Transform: Data Cleaning

# Drop rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create derived columns
df["year"] = df["InvoiceDate"].dt.year
df["month"] = df["InvoiceDate"].dt.month

# Calculate total price
df["total_price"] = df["Quantity"] * df["UnitPrice"]

# Remove invalid records
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]


# Load: Write cleaned data to S3 (Parquet)

buffer = BytesIO()
df.to_parquet(buffer, index=False)
buffer.seek(0)

s3.put_object(
    Bucket=S3_BUCKET,
    Key=CLEAN_KEY,
    Body=buffer.getvalue()
)

print("ETL completed successfully. Clean data written to S3.")
