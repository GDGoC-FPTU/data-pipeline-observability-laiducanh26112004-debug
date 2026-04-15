"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-XXXX  (<-- Thay XXXX bang ma so cua ban)
Name: Your Name Here

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.
    """
    print(f"Extracting data from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category')

        if price > 0 and category and str(category).strip() != "":
            valid_records.append(record)
        else:
            error_count += 1

    print(f"Validation complete: {len(valid_records)} valid, {error_count} invalid")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.
    """
    if not data:
        return None

    df = pd.DataFrame(data)

    # discounted price
    df['discounted_price'] = df['price'] * 0.9

    # normalize category
    df['category'] = df['category'].astype(str).str.title()

    # timestamp
    df['processed_at'] = datetime.datetime.now().isoformat()

    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            print(f"\nPipeline completed! {len(final_df)} records saved.")
        else:
            print("\nTransform returned None. Check your transform() function.")
    else:
        print("\nPipeline aborted: No data extracted.")
