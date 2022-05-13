
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('simulator/pv_results.csv')
# print(df.head())
# print(len(df))

df_new = df[['Time', 'Simulator']]
# print(df_new.head())
# print(len(df_new))

plt.plot(df_new['Time'], df_new['Simulator'])
plt.savefig('first.png')
plt.show()

# plt.interactive(False)


