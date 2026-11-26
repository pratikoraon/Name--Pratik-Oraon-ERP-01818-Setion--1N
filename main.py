import os

import matplotlib.pyplot as plt
import pandas as pd

FILE = "sales.csv"


def load_and_clean_data():
    if not os.path.exists(FILE):
        print(f"Error: {FILE} not found!")
        return None

    # Read CSV
    try:
        df = pd.read_csv(FILE)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    # Check required columns
    required = ['Date', 'Product', 'Region', 'Quantity', 'Amount']
    if not all(col in df.columns for col in required):
        print(f"Error: CSV must have columns: {required}")
        return None

    # Remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    if before != len(df):
        print(f"{before - len(df)} duplicate row(s) removed.")

    # Convert Quantity and Amount to numbers; invalid values become NaN
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

    # Report invalid rows using the original raw values
    invalid_rows = df[df['Quantity'].isna() | df['Amount'].isna()]
    if not invalid_rows.empty:
        raw_df = pd.read_csv(FILE, dtype=str)
        for idx in invalid_rows.index:
            # idx is the 0-based data row, so +1 gives the data row number
            if pd.isna(df.loc[idx, 'Amount']):
                col = 'Amount'
            else:
                col = 'Quantity'
            bad_val = raw_df.loc[idx, col]
            print(f"Row {idx + 1} skipped: invalid {col} '{bad_val}'")

    df = df.dropna(subset=['Quantity', 'Amount'])
    df = df[df['Quantity'] > 0]
    df = df[df['Amount'] > 0]

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    return df


def show_summary(df):
    total_revenue = df['Amount'].sum()
    transactions = len(df)
    units_sold = int(df['Quantity'].sum())
    top_product = df.groupby('Product')['Quantity'].sum().idxmax()

    print("\n--- SUMMARY ---")
    print(f"Total Revenue: {int(total_revenue)} | Transactions: {transactions} "
          f"| Units sold: {units_sold} | Top product: {top_product}")


def plot_region_chart(df):
    region_sales = df.groupby('Region')['Amount'].sum()
    plt.figure(figsize=(8, 5))
    region_sales.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Region-wise Sales')
    plt.xlabel('Region')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def group_by_product_region(df):
    print("\n--- GROUP BY PRODUCT ---")
    prod = df.groupby('Product')['Amount'].sum()
    for product, amount in prod.items():
        print(f"{product}: {int(amount)}")

    print("\n--- GROUP BY REGION ---")
    reg = df.groupby('Region')['Amount'].sum()
    for region, amount in reg.items():
        print(f"{region}: {int(amount)}")

    # Show the 'Region-wise Sales' bar chart
    plot_region_chart(df)


def top_5_products(df):
    print("\n--- TOP 5 SELLING PRODUCTS ---")
    top5 = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
    print(top5.to_string())


def plot_charts(df):
    # 1. Bar chart - region-wise sales
    plot_region_chart(df)

    # 2. Line chart - date-wise sales trend
    date_sales = df.groupby('Date')['Amount'].sum()
    plt.figure(figsize=(8, 5))
    date_sales.plot(kind='line', marker='o', color='green')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 3. Bar chart - top 5 selling products
    prod_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    prod_sales.plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Top 5 Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def main():
    df = load_and_clean_data()
    if df is None or df.empty:
        print("No valid data to analyse.")
        return

    while True:
        print("\n===== SALES DATA ANALYZER =====")
        print("1. Summary")
        print("2. Group by Product & Region")
        print("3. Top 5 Selling Products")
        print("4. Plot Charts (Bar and Line)")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            show_summary(df)
        elif choice == '2':
            group_by_product_region(df)
        elif choice == '3':
            top_5_products(df)
        elif choice == '4':
            plot_charts(df)
        elif choice == '5':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()