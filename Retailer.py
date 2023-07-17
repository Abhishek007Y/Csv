import tabula
import pandas as pd
import numpy as np
    # Use the read_pdf function to extract tabular data
    # The pages parameter specifies which pages to extract data from
    # Setting pages='all' will extract data from all pages
def RetailerStatement(file_path):
    # Use the read_pdf function to extract tabular data
    # The pages parameter specifies which pages to extract data from
    # Setting pages='all' will extract data from all pages
    tabular_data = tabula.read_pdf(file_path, pages='all')
    
    # Combine all the tabular data into a single 2D numpy array
    arr_list = [df.values for df in tabular_data]
    arr = np.vstack(arr_list)

    # Define the column names
    column_names = ['Particular', '₹ Amount', 'Credit', 'Debit', 'Balance', 'Date']

    # Convert the 2D array to a list of dictionaries
    result_list = [dict(zip(column_names, row)) for row in arr.tolist()]
    # print(result_list)
    
    return result_list

