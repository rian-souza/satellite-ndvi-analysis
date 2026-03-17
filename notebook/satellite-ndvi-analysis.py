!pip install rasterio earthpy

import numpy as np
import matplotlib.pyplot as plt
import rasterio
import earthpy as et
import os
import seaborn as snc

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

sns.set_theme(style="whitegrid", context="talk")
plt.rcParams["figure.figsize"] = (10, 6)
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("Mapa NDVI da Área Observada")
plt.axis("off")
plt.show()

ndvi_clean = ndvi[~np.isnan(ndvi)]

plt.figure()
sns.histplot(
    ndvi_clean,
    bins=50,
    kde=True
)
plt.title("Distribuição dos Valores de NDVI")
plt.xlabel("NDVI")
plt.ylabel("Frequência")
plt.show()

ndvi_classes = np.zeros_like(ndvi)
ndvi_classes[ndvi < 0] = 0
ndvi_classes[(ndvi >= 0) & (ndvi < 0.2)] = 1
ndvi_classes[(ndvi >= 0.2) & (ndvi < 0.5)] = 2
ndvi_classes[ndvi >= 0.5] = 3

print("Classificação criada com sucesso.")
