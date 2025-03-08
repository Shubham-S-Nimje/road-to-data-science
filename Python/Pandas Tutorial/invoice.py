import pandas as pd

# Define the orders data (without CardUrl column)
orders_data = {
    "Id": [11015, 11013, 11012, 11011, 11010, 11008, 11006, 11004, 11003, 11002],
    "OrderId": ["O1728905954145", "O1728905369257", "O1728905339724", "O1728904920192", "O1728903368159", "O1728900698765", "O1728898315967", "O1728892908128", "O1728892796392", "O1728892526760"],
    "UserId": [1728905954, 1728905369, 1728905339, 1728904920, 1728903368, 1728900698, 1728898315, 1728892908, 1728892796, 1728892526],
    "DesignId": [5954, 5369, 5339, 4920, 3368, 698, 8315, 2908, 2796, 2526],
    "PaymentId": ["T1728905962839", "T1728905376317", "T1728905344431", "T1728905901438", "T1728903377662", "T1728900702075", "T1728898322191", "O1728886062953", "T1728892814648", "T1728892528109"],
    "Language": ["marathi", "marathi", "hindi", "marathi", "marathi", "marathi", "marathi", "marathi", "english", "english"],
    "DesignName": [
        "Dohale jevan invitation card online free - EasyInvite", 
        "Engagement invitation card maker in marathi (Free Online)",
        "Free Download: Hindi Shok Sandesh Invitations - Easy Invite", 
        "Marathi Birthday Invitation Card for 2nd Birthday - Editable", 
        "Dohale jevan invitation card online free - EasyInvite", 
        "Buddhist wedding invitation card in marathi free - EasyInvite", 
        "Engagement invitation card maker in marathi (Free Online)", 
        "Free Marathi Javal Kadne Invitations | Easy Invite",
        "Effortless Wedding Invitation Design at EasyInvite - EasyInvite", 
        "Creative Engagement Invitation - Free Name Editing!"
    ],
    "Amount": [29, 29, 29, 49, 29, 49, 29, 29, 29, 49],
    "Created At": ["10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024"],
    "Updated At": ["10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024", "10/14/2024"]
}

# Define the transactions data
transactions_data = {
    "MerchantId": ["M1D8ZVIZDMKW"]*10,
    "TransactionType": ["FORWARD_TRANSACTION"]*10,
    "MerchantOrderId": ["O1728905954145", "O1728904920192", "O1728905369257", "O1728905339724", "O1728903368159", "O1728900698765", "O1728898315967", "O1728892796392", "O1728892526760", "O1728886062953"],
    "PhonePeTransactionId": ["T2410141709481488778262", "T2410141708416919433384", "T2410141659449112242249", "T2410141659219214682226", "T2410141626408925564984", "T2410141542015406447920", "T2410141502172622566493", "T2410141330463782462566", "T2410141325385571585306", "T2410141323389987675495"],
    "TransactionUTR": ["9.278E+11", "4.28899E+11", "4.65428E+11", "4.65475E+11", "4.65484E+11", "4.65406E+11", "4.65428E+11", "4.28875E+11", "4.65497E+11", "4.28833E+11"],
    "TotalTransactionAmount": [29, 49, 29, 29, 29, 49, 29, 29, 49, 29],
    "TransactionDate": ["14-10-2024 17:09", "14-10-2024 17:08", "14-10-2024 16:59", "14-10-2024 16:59", "14-10-2024 16:26", "14-10-2024 15:42", "14-10-2024 15:02", "14-10-2024 13:30", "14-10-2024 13:25", "14-10-2024 13:23"],
    "TransactionStatus": ["COMPLETED"]*10,
    "UPIAmount": [29, 49, 29, 29, 29, 49, 29, 29, 49, 29]
}

# Create the DataFrames
orders_df = pd.DataFrame(orders_data)
transactions_df = pd.DataFrame(transactions_data)

# Write to Excel without "CardUrl"
with pd.ExcelWriter('sample_invoice_data.xlsx', engine='xlsxwriter') as writer:
    orders_df.to_excel(writer, sheet_name='Orders', index=False)
    transactions_df.to_excel(writer, sheet_name='Transactions', index=False)

print("Data has been written to 'sample_invoice_data.xlsx'")
