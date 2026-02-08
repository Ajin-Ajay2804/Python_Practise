import csv

file_path = 'D:\GIS Programming\Project\lst_data.csv'

lst_values = []
ndvi_values = []

with open(file_path, 'r') as file:
    reader = csv. DictReader(file)

    for row in reader:
        lst = float(row['LST'])
        ndvi = float(row['NDVI'])


        lst_values.append(lst)
        ndvi_values.append(ndvi)

print('Total Pixels:', len(lst_values))
print('Average LST:', sum(lst_values)/len(lst_values))
print('Average NDVI:', sum(ndvi_values)/len(ndvi_values))

print("\nHigh LST & Low NDVI Pixels:")

for i in range(len(lst_values)):
    if lst_values[i] > 32 and ndvi_values[i] < 0.4:
        print(f"Pixel {i+1} → LST: {lst_values[i]}, NDVI: {ndvi_values[i]}")


output_file = 'D:\GIS Programming\Project\Outputs\high_uhi_pixels.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Pixel_ID', 'LST', 'NDVI'])

    for i in range(len(lst_values)):
        if lst_values[i] > 32 and ndvi_values[i] < 0.4:
            writer.writerow([i+1, lst_values[i], ndvi_values[i]])

print("\nHigh UHI pixels saved to: {output_file}")