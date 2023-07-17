import camelot
# import xlwt
# password = "6983827427"


def HdfcStatement(pdf_file_path):

    data = camelot.read_pdf(pdf_file_path,pages='all',flavour='lattice')



    table_data = []

    
    column_names = ['Date', 'Narration', 'Cheque/Ref. No.', 'Value Date', 'Withdrawal', 'Deposit','Closing Balance']


    for table in data:
            # Convert the table to a Pandas DataFrame
            df = table.df
            
            # Extract the data from the DataFrame
            # arr = df.values
            arr = df.replace('\n', '', regex=True).values


            # Define the column names
                
            # Convert the 2D array to a list of dictionaries
            result_list = [dict(zip(column_names, row)) for row in arr[1:].tolist()]

            # Add the extracted data to the list of table data
            table_data.append(result_list)
        


    return table_data
