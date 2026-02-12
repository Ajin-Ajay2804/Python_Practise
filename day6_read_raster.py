import rasterio 
import numpy as np

raster_path = "D:\GIS Programming\Data\lst_sample.tif"

with rasterio.open(raster_path) as src:
    lst_array = src.read(1)
    nodata_value = src.nodata

    print("Raster shape:", lst_array.shape)
    print("CRS:", src.crs)
    print("Bounds:", src.bounds)
    #print("NoData value:", nodata_value)

# Remove NoData properly
if nodata_value is not None:
    lst_array = lst_array[lst_array != nodata_value]

# Also remove extreme invalid values
lst_array = lst_array[np.isfinite(lst_array)]

print("\nMaximum LST:", np.max(lst_array))
print("Minimum LST:", np.min(lst_array))
print("Mean LST:", np.mean(lst_array))

high_temp_pixels = np.sum(lst_array > 32)
print("High temperature pixel count:", high_temp_pixels)

