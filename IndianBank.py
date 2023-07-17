import camelot 

def IndianBankStatement(pdf_file_path,password):

    data=camelot.read_pdf(pdf_file_path,password=password,pages='all',flavour='lattice')

    table_data=[]

    column_names = ['TRANSACTION DATE', 'PARTICULARS', 'WITHDRAWLS', 'DEPOSIT', 'BALANCE']

    for tables in data:
        df=tables.df
        arr=df.replace('\n','',regex=True).values
        result_list=[dict(zip(column_names,row)) for row in arr.tolist() if row[1] not in ['', 'PARTICULARS']]
        table_data.append(result_list)


    return table_data