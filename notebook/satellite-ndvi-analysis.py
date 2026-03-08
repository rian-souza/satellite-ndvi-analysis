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

red_path = "/root/earth-analytics/data/ndvi-automation/sites/SJER/landsat-crop/LC080420342017061601T1-SC20181023152417/LC08_L1TP_042034_20170616_20170629_01_T1_sr_band4.tif"
nir_path = "/root/earth-analytics/data/ndvi-automation/sites/SJER/landsat-crop/LC080420342017061601T1-SC20181023152417/LC08_L1TP_042034_20170616_20170629_01_T1_sr_band5.tif"

red = rasterio.open(red_path)
nir = rasterio.open(nir_path)

red_band = red.read(1)
nir_band = nir.read(1)

print("Dimensão da imagem:", red_band.shape)

red_band = red_band.astype(float)
nir_band = nir_band.astype(float)

np.seterr(divide='ignore', invalid='ignore')

ndvi = (nir_band - red_band) / (nir_band + red_band)

ndvi = np.clip(ndvi, -1, 1)

ndvi_min = np.nanmin(ndvi)
ndvi_max = np.nanmax(ndvi)

print(f"NDVI mínimo: {ndvi_min:.4f}")
print(f"NDVI máximo: {ndvi_max:.4f}")
