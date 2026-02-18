import rasterio
import numpy as np

with rasterio.open(r"D:\GIS Programming\Data\NDVI.tif") as src:
    raster = src.read(1)
    meta = src.meta


nodata = src.nodata
if nodata is not None :
    raster = np.where(raster == nodata, np.nan, raster)

print('Minimum:', np.nanmin(raster))
print('Maximum', np.nanmax(raster))
print('Mean', np.nanmean(raster))

mask = np.where(raster > 0.3,1,0)

meta.update(dtype=rasterio.uint8,nodata=0)

with rasterio.open(r'D:\GIS Programming\Project\Outputs\masked_output.tif','w', **meta) as dst:
    dst.write(mask.astype(rasterio.uint8),1)

print('Masked raster successfully')