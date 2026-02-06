import numpy as np

lst_array = np.array([
    [30.5,31.2,32.8],
    [29.9,33.1,34.0],
    [28.7,30.0,31.5]
])

print('LST Raster (Array): \n', lst_array)

print('\nRaster Shape (rows, columns):', lst_array.shape)
print('Maximum LST:', np.max(lst_array))
print('Minimum LST:',np.min(lst_array))
print('Mean LST:',np.mean(lst_array))

high_temp = lst_array > 32

print('\nHigh Temperature Zones (True = High):\n', high_temp)


high_count = np.sum(lst_array > 32)
total_pixels = lst_array.size

print('\nHigh Temperature Pixel Count:',high_count)
print('Total Pixels:',total_pixels)
print('Percentage of High Temperature area:', high_count/total_pixels*100, '%')


