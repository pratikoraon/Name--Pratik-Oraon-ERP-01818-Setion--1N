# Sales Data Analyzer (PS No. 92)

A Python 3 console program that analyses a sales CSV file to find total revenue, best-selling products and region-wise performance, and visualises the results with Matplotlib.

**Concepts:** Pandas, CSV, Matplotlib, Grouping

## Features

- Reads `sales.csv` with Pandas and validates the required columns
- Removes duplicate rows and skips invalid rows (non-numeric, zero or negative Quantity/Amount, bad dates)
- Summary: total revenue, transactions, units sold, top product
- `groupby()` for product-wise and region-wise sales
- Top 5 selling products
- Charts: region-wise bar chart, date-wise line chart, top 5 products bar chart

## CSV Format

```
Date,Product,Region,Quantity,Amount
2026-08-01,Laptop,North,2,100000
```

## Requirements

```
pip install pandas matplotlib
```

## How to Run

Place `sales.csv` in the same folder as the script, then:

```
python sales_analyzer.py
```

Menu:

```
1. Summary
2. Group by Product & Region
3. Top 5 Selling Products
4. Plot Charts (Bar and Line)
5. Exit
```

## Test Cases

Each test case has its own folder inside `tests/` containing:

- `sales.csv` - input data
- `input.txt` - menu choices fed to the program
- `expected_output.txt` - expected result

To run a test (example: test1):

```
cd tests/test1
python ../../sales_analyzer.py < input.txt
```

### Test Case 1: Normal Input (`tests/test1`)

`sales.csv`:
```
2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,5000
2026-08-03,Laptop,South,1,50000
```
Menu option: 1 (Summary)

Expected output:
```
Total Revenue: 155000 | Transactions: 3 | Units sold: 13
```

### Test Case 2: Boundary / Minimum Input (`tests/test2`)

`sales.csv`: 1 row only
```
2026-08-01,Mouse,North,1,500
```
Menu option: 1 (Summary)

Expected output:
```
Total Revenue: 500 | Transactions: 1 | Top product: Mouse
```

### Test Case 3: Invalid Input (`tests/test3`)

`sales.csv`:
```
2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,abc
2026-08-03,Laptop,South,1,50000
```
Menu option: 1 (Summary)

Expected output:
```
Row 2 skipped: invalid Amount 'abc'
Total Revenue: 150000 | Transactions: 2
```

### Test Case 4: Different Valid Scenario (`tests/test4`)

Same CSV as Test Case 1. Menu option: 2 (Group by Product & Region)

Expected output:
```
Laptop: 150000 | Mouse: 5000
North: 100000 | South: 55000
Bar chart 'Region-wise Sales' displayed
```

### Actual program output

The program prints Units sold and Top product together in the summary line, so the actual output contains the expected values plus the extra field:

```
Total Revenue: 155000 | Transactions: 3 | Units sold: 13 | Top product: Mouse
```

## Project Structure

```
sales-data-analyzer/
├── sales_analyzer.py
├── README.md
└── tests/
    ├── test1/  (sales.csv, input.txt, expected_output.txt)
    ├── test2/
    ├── test3/
    └── test4/
```
