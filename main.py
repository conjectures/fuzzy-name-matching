import matplotlib.pyplot as plt
import pandas as pd
import os

filename = 'usa_names_2010.csv'

if os.path.exists(filename):
    df = pd.read_csv(filename).head(50)

    # pivot_table = df.pivot(index="name", values="total_count")
    # df[::2].plot.bar(x="name", y="total_count")
    # df[1::2].plot.bar(x="name", y="total_count")
    df.plot.bar(x="name", y="total_count", colormap='Paired')
    plt.show()

# pivot_table = df.pivot(index="year", columns="plurality", values="count")
# pivot_table.plot(kind="bar", stacked=True, figsize=(15, 7) )
# plt.show()
