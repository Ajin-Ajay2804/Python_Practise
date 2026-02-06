lst_values = [30.5,31.2,32.8,29.9,33.1]

print('/nLST Values:', lst_values)
print('Maximum LST:', max(lst_values))
print('Minimum LST:', min(lst_values))
print('Average LST:',sum(lst_values)/len(lst_values))


for temp in lst_values:
    if temp > 32:
        print(temp, '-> High Temperature Zone')
    else:
        print(temp, '-> Low Temperature Zone')