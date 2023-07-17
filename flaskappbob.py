import os
import numpy as np
import pandas as pd
from tabula import read_pdf
import json
from flask import Flask, request
from ucobank import UcobankStatement
from Retailer import RetailerStatement
from hdfc import HdfcStatement
from IndianBank import IndianBankStatement

app = Flask(__name__)   

def process_bob_data(file_path):
    df_list = read_pdf(file_path, pages='all')
    arr_list = [df.values for df in df_list]
    arr = np.vstack(arr_list)

    keys = ['date', 'description', 'amount', 'type']
    data = []
    for row in arr:
        row_data = dict(zip(keys, row))
        row_data['date'] = row_data['date']
        row_data['amount'] = float(row_data['amount'].replace(',', ''))
        data.append(row_data)
    return data
    

@app.route('/', methods=['POST'])
def upload_file():
    partner_name = request.form.get('partnerName', '').lower()  # Get the partner name from request body
    if not partner_name:
        return 'Partner name is missing', 400
    
    password=request.form.get('password','').lower()

    file = request.files.get('file')
    if not file:
        return 'File is missing', 400

    filename = file.filename
    file_path = os.path.join(os.getcwd(), filename)
    file.save(file_path)

    if partner_name == 'bob':
        processed_data = process_bob_data(file_path)
        # json_data = json.dumps(processed_data)
        return processed_data

    
    if partner_name=='uco':
        processed_data=UcobankStatement(file_path)
        # json_data = json.dumps(processed_data)
        return processed_data
    
    if partner_name=='retailer':
        processed_data=RetailerStatement(file_path)
        # json_data=json.dumps(processed_data)
        return processed_data
    
    if partner_name=='hdfc':
        processed_data=HdfcStatement(file_path)
        # json_data=json.dumps(processed_data)
        return processed_data
    if partner_name=='indian bank':
        processed_data=IndianBankStatement(file_path,password)

        return processed_data


    else:
        return 'Partner name not supported', 400


    return '''
    <!doctype html>
    <html>
        <body>
            <h1>Upload a PDF file</h1>
            <form method=post enctype=multipart/form-data>
                <input type=file name=file>
                <input type=submit value=Upload>
            </form>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
