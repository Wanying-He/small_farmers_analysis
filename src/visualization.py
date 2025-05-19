
# visualization.py
# Author: Yetta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_yield_by_region(df):
    """Generate a bar plot of crop yield by region."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Region', y='Crop_Yield', data=df)
    plt.title('Average Crop Yield by Region')
    plt.show()

def plot_ict_vs_yield(df):
    """Generate a plot of ICT adoption vs. Crop Yield."""
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='ICT_Adoption', y='Crop_Yield', data=df)
    plt.title('ICT Adoption vs. Crop Yield')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/simulated_farmers_data.csv')
    plot_yield_by_region(df)
    plot_ict_vs_yield(df)
