import rasterio
import numpy as np
import matplotlib.pyplot as plt

raster_path = "D:\GIS Programming\Data\lst_sample.tif"

with rasterio.open(raster_path) as src :
    lst_array = src.read(1)
    nodata_value = src.nodata


if nodata_value is not None:
    lst_array = np.where(lst_array == nodata_value, np.nan, lst_array)


plt.figure()
plt.imshow(lst_array,cmap= 'viridis')
plt.colorbar(label= "LST (°C)")
plt.title('Land Surface Temperature Map')
plt.xlabel('Column Index')
plt.ylabel('Row Index')

plt.savefig('D:\GIS Programming\Project\Outputs\lst_map.png')
plt.close()
