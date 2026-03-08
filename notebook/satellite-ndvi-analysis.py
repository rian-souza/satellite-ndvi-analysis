!pip install rasterio earthpy

import numpy as np
import matplotlib.pyplot as plt
import rasterio
import earthpy as et
import os

data = et.data.get_data("ndvi-automation")
print(data)

data_path = et.data.get_data("ndvi-automation")

for root, dirs, files in os.walk(data_path):
    for file in files:
        if file.endswith(".tif"):
            print(os.path.join(root, file))

for root, dirs, files in os.walk(data_path):
    print(root)
