import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


def generate_samples(
        input_file='data/usa_names_2010.csv',
        samples_file='data/name_samples.csv'
        ):
    # filename = 'data/usa_names_2010.csv'
    num_slice = 5000
    samples = 200000

    try:
        df = pd.read_csv(input_file).head(num_slice)
        total_name_occurences = df.total_count.sum()
        df.total_count = (df.total_count / total_name_occurences) * 100

        names = df.iloc[1::2, :].reset_index().drop(['index'], axis=1)
        surnames = df.iloc[::2, 0::2].reset_index().drop(['index'], axis=1)

        # print(f'Total name occurences: {total_name_occurences}')
        # names = df[::2].plot.bar(x="name", y="total_count")
        # surnames = df[1::2].plot.bar(x="name", y="total_count")
        # df.plot.bar(x="name", y="total_count", color=['C0', 'C1'])
        # plt.show()

        # Sample columnds
        sampled_names = names.sample(n=samples, weights='total_count', random_state=random.randint(0,1000), replace=True)
        sampled_surnames = surnames.sample(n=samples, weights='total_count', random_state=random.randint(0,1000), replace=True)
        # Rename column
        sampled_names = sampled_names.reset_index().drop(['index', 'total_count'], axis=1)
        sampled_surnames = sampled_surnames.reset_index().drop(['index', 'total_count'], axis=1)

        # smpl = pd.concat([sampled_names, sampled_surnames], axis=1)
        smpl = sampled_names.reset_index().drop(['index'], axis=1)

        smpl["name"] = sampled_names["name"] + " " + sampled_surnames["name"]
        # smpl["name"] = smpl[["name", "surname"]].agg(' '.join, axis=1)
        print(smpl)
        print("Duplicated name?")
        boolean = smpl['name'].duplicated().any()
        print(boolean)

        smpl.to_csv('data/name_samples.csv', index=False)


    except FileNotFoundError:
        print("File not Found. Exiting.")

if __name__ == "__main__":
    generate_samples()
