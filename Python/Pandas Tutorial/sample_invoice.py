import pandas as pd
from datetime import datetime

# Sample data for the invoice
invoice_data = {
    "Description": [
        "Design Name: Dohale jevan invitation card online free - EasyInvite",
        "Language: Marathi",
        "Order ID: O1728905954145",
        "User ID: 1728905954",
        "Design ID: 5954",
        "Payment ID: T1728905962839",
        "Amount: ₹29",
    ],
    "Details": [
        "Marathi Dohale Jevan Invitation Card",
        "Marathi",
        "O1728905954145",
        "1728905954",
        "5954",
        "T1728905962839",
        "₹29"
    ]
}

# Create DataFrame for the invoice
invoice_df = pd.DataFrame(invoice_data)

# Summary info (order and transaction details)
summary_info = {
    "Invoice Number": ["INV-20241014-001"],
    "Date": [datetime.now().strftime('%Y-%m-%d')],
    "Order ID": ["O1728905954145"],
    "Transaction ID": ["T2410141709481488778262"],
    "Amount": ["₹29"],
    "Transaction Status": ["COMPLETED"]
}

# Create DataFrame for the summary
summary_df = pd.DataFrame(summary_info)

# Write the data to Excel
file_path = 'sample_invoice.xlsx'
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    summary_df.to_excel(writer, sheet_name='Invoice', startrow=0, index=False)
    invoice_df.to_excel(writer, sheet_name='Invoice', startrow=5, index=False)

print(f"Invoice created at {file_path}")
