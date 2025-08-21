# Student Budget Planner

A Streamlit web app to help students plan, track, and analyze their monthly finances. Easily add manual entries or upload your bank account statement in Excel format for automatic categorization and insightful analysis.

## Features

- **Add/Edit Income & Expenses:**
  - Manually add or edit income and expense entries with category and type.
  - Real-time table with edit/delete options.

- **Bank Statement Upload & Auto-Categorization:**
  - Upload your account statement in Excel format (`.xlsx` or `.xls`).
  - The app analyzes the Description field and assigns categories (Food, Travel, Shopping, Bills, Wallet/UPI, Income, etc.) using a keyword lookup.
  - Edit categories for any transaction after upload.

- **Monthly Summary & Analysis:**
  - See total income, expenses, and savings for the month.
  - Category-wise breakdown for both income and expenses.
  - Visualizations: Pie and bar charts for category distributions.

- **Export:**
  - Download your monthly report (including category summary) as a CSV file.

## How to Use

1. **Install Requirements**
   - Python 3.8+
   - Install dependencies:
     ```bash
     pip install streamlit pandas matplotlib openpyxl
     ```

2. **Run the App**
   ```bash
   streamlit run budget_planner.py
   ```

3. **Add Entries or Upload Statement**
   - Use the form to add manual entries, or upload your bank statement (Excel) for auto-categorization.
   - Edit categories as needed.

4. **Analyze & Export**
   - View your monthly summary, category analysis, and download the report.

## Supported Bank Statement Format

- Excel file with columns:
  - `Txn Date`, `Description`, `Debit`, `Credit`, `Balance`
- The app will try to auto-detect debit/credit columns. If your file uses different names, you may need to adjust the code or rename columns.

## Customization

- Expand the `CATEGORY_LOOKUP` dictionary in `budget_planner.py` to add more merchants or keywords for better auto-categorization.

## License

MIT License
