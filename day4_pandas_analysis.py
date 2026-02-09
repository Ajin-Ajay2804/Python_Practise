import pandas as pd

df = pd.read_csv('D:\GIS Programming\Project\lst_data.csv')

print('First 5 rows:')
print(df.head())

print('\nSummary Statistics:')
print(df.describe())

uhi_pixels = df[(df['LST'] > 32)& (df['NDVI'] < 0.4)]

print('\nHigh UHI Pixels:')
print(uhi_pixels)

output_path = 'D:\GIS Programming\Project\Outputs\high_uhi_pixels_pandas.csv'
uhi_pixels.to_csv(output_path, index=False)

print('\nSaved:', output_path)


print('\nMean LST:', df['LST'].mean())
print('Max NDVI:',df['NDVI'].max())

