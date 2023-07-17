import tabula
import pandas as pd
import numpy as np

def UcobankStatement(pdf_file_path):
    # Use the read_pdf function to extract tabular data
    # The pages parameter specifies which pages to extract data from
    # Setting pages='all' will extract data from all pages
    tabular_data = tabula.read_pdf(pdf_file_path, pages='all')
    
    refined_data = {}

    # Loop through each table in the extracted tabular data
    for table in tabular_data:
        # Loop through each column in the table
        for column in table.columns:
            # Get the column name
            column_name = column.strip()

            # Check if the column name already exists in the refined data dictionary
            if column_name in refined_data:
                # If the column name exists, append the column data to the existing list
                # and fill in with None or NaN to make sure all columns have the same length
                refined_data[column_name].extend(table[column])
                col_length = len(refined_data[column_name])
                missing_values = col_length - len(table[column])
                if missing_values > 0:
                    refined_data[column_name].extend([None] * missing_values)  # use None for object dtype, NaN for numeric dtype
            else:
                # If the column name does not exist, create a new list with the column data
                refined_data[column_name] = list(table[column])

    # Replace all NaN values with an empty string
    df = pd.DataFrame.from_dict(refined_data).replace(np.nan, '', regex=True)
    df = df[df.apply(lambda row: not all(row == ''), axis=1)]
    df_combined = pd.concat([df.shift(-1), df], axis=1).iloc[:-1]

    transactions=[]
    part=""
    date=""
    Withdraw=""
    Deposits=""
    Balance=""
    partIndex=1
    DateIndex=1
    WithdrawlsIndex=1
    DepositsIndex=1
    BalanceIndex=1

    for index, row in df.iterrows():
        transaction={}
        for column_name, column_value in row.items():
            if column_name=="Instrument No":
                continue
            if column_name=="Date":
                if DateIndex==1:
                    date=column_value
                    DateIndex+=1
                else:
                    transaction['Date']=date
                    DateIndex=1

            if column_name=="Particulars":
                if partIndex==1:
                    part=column_value
                    partIndex+=1
                else:
                    part=part+column_value
                    partIndex=1
                    transaction['Description']=part

            if column_name=="Withdrawals":
                if WithdrawlsIndex==1:
                    Withdraw=column_value
                    WithdrawlsIndex+=1
                else:
                    transaction['Witdrawals']=Withdraw
                    WithdrawlsIndex=1

            if column_name=="Deposits":
                if DepositsIndex==1:
                    Deposits=column_value
                    DepositsIndex+=1
                else:
                    transaction['Deposits']=Deposits
                    DepositsIndex=1

            if column_name=="Balance":
                if BalanceIndex==1:
                    Balance=column_value
                    BalanceIndex+=1
                else:
                    transaction['Balance']=Balance
                    if date!="":
                        transactions.append(transaction)
                    BalanceIndex=1
    return transactions
