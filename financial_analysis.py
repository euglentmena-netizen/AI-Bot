import pdfplumber
import pandas as pd
import numpy as np
from pathlib import Path

# PDF file path
pdf_path = "FY25_Q2_Consolidated_Financial_Statements.pdf"

print("=" * 80)
print("FINANCIAL ANALYSIS - KPI & RECOMMENDATIONS")
print("=" * 80)
print()

# Extract data from PDF
try:
    with pdfplumber.open(pdf_path) as pdf:
        print(f"PDF loaded successfully. Total pages: {len(pdf.pages)}")
        print()
        
        # Extract tables from all pages
        all_tables = []
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            if tables:
                print(f"Page {i+1}: Found {len(tables)} table(s)")
                for table_idx, table in enumerate(tables):
                    all_tables.append(table)
                    # Display first few rows of each table
                    print(f"\nTable {table_idx + 1} Preview:")
                    df = pd.DataFrame(table[1:], columns=table[0]) if len(table) > 0 else pd.DataFrame(table)
                    print(df.head())
                    print()
        
        if all_tables:
            print(f"\nTotal tables extracted: {len(all_tables)}")
        
        # Extract text from pages
        print("\n" + "=" * 80)
        print("EXTRACTED TEXT FROM PDF:")
        print("=" * 80)
        for i, page in enumerate(pdf.pages[:2]):  # Show first 2 pages
            print(f"\n--- PAGE {i+1} ---")
            text = page.extract_text()
            print(text[:1000])  # Print first 1000 chars
            
except Exception as e:
    print(f"Error reading PDF: {e}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
