import numpy as np
import pandas as pd
from tabula import read_pdf
import json

url = 'pdf-1682486297490.pdf'
df_list = read_pdf(url, pages='all')

# Convert each DataFrame object in the list to a NumPy array
arr_list = [df.values for df in df_list]

# Stack the NumPy arrays vertically to create a single 2D array
arr = np.vstack(arr_list)
keys = ['date', 'description', 'amount', 'type']
data = [dict(zip(keys, row)) for row in arr]


print(arr)


json_data = json.dumps(data)

# Print JSON data
print(json_data)