import tabula
import pandas as pd
import numpy as np

file_path="Komal-Password-6983827427.pdf"
password="6983827427"
tabular_data = tabula.read_pdf(file_path, pages='all',password=password)

print(type(tabular_data[1]))
print(tabular_data[0])

    # Combine all the tabular data into a single 2D numpy array
# arr_list = [df.values for df in tabular_data]
# arr = np.vstack(arr_list)
# print(arr)