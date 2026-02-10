import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\GIS Programming\Project\lst_data.csv')

plt.figure()
plt.plot(df['Pixel_ID'], df['LST'])
plt.xlabel('Pixels ID')
plt.ylabel('LST °C')
plt.title('Land Surface Temperature Variation')
plt.show()

plt.figure()
plt.scatter(df['NDVI'], df['LST'])
plt.xlabel('NDVI')
plt.ylabel('LST °C')
plt.title('LST vs NDVI Relationship')
plt.show()

plt.savefig('D:\GIS Programming\Project\Outputs\lst_profile.png')
plt.savefig('D:\GIS Programming\Project\Outputs\lst_vs_ndvi.png')

plt.figure()
plt.savefig('D:\GIS Programming\Project\Outputs')
plt.close()
