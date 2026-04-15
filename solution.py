"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-XXXX
Name: Your Name Here
==============================================================
"""

import json
import pandas as pd
import os
from datetime import datetime
import logging

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'
LOG_FILE = 'etl.log'

# --- LOGGING SETUP ---
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.
    """
    logging.info(f"Extracting data from {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info(f"Extracted {len(data)} records")
        return data
    except FileNotFoundError:
        logging.error(f"File {file_path} not found")
        return []
    except json.JSONDecodeError:
        logging.error("Invalid JSON format")
        return []


def validate(data):
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category')

        if price > 0 and category and str(category).strip() != "":
            valid_records.append(record)
        else:
            error_count += 1

    # ✅ BẮT BUỘC có print này
    print(f"Validation summary: {len(valid_records)} valid, {error_count} invalid")

    # logging vẫn giữ
    logging.info(f"processed={len(valid_records)}")
    logging.info(f"dropped={error_count}")

    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.
    """
    # luôn trả DataFrame (không return None)
    df = pd.DataFrame(data)

    if df.empty:
        return df

    # discounted price
    df['discounted_price'] = df['price'] * 0.9

    # normalize category
    df['category'] = df['category'].astype(str).str.title()

    # timestamp (KHÔNG dùng isoformat)
    df['processed_at'] = datetime.now()

    logging.info(f"Transformed {len(df)} records")

    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    df.to_csv(output_path, index=False)
    logging.info(f"Saved {len(df)} records to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    logging.info("=== ETL Pipeline Started ===")

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if not final_df.empty:
            load(final_df, OUTPUT_FILE)
            logging.info(f"Pipeline completed: {len(final_df)} records saved")
        else:
            logging.warning("No data after transform")
    else:
        logging.error("Pipeline aborted: No data extracted")