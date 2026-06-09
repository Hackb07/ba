# Experiment 4: OLAP Operations using Pandas
# Aim: To perform OLAP operations (Drill-down, Slice, Dice) using Pandas DataFrame.

import pandas as pd

data = pd.DataFrame({
'Region':['North','South','North','East','South'],
'Product':['A','B','A','B','A'],
'Sales':[100,200,150,300,250]
})

# Drill Down
print("Drill Down")
print(data.groupby('Region')['Sales'].sum())

# Slice
print("\nSlice (South Region)")
print(data[data['Region']=="South"])

# Dice
pivot = pd.pivot_table(data, values='Sales',
                       index='Region',
                       columns='Product',
                       aggfunc='sum')

print("\nDice Operation")
print(pivot)
