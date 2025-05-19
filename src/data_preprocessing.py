
# data_preprocessing.py
# Author: Yetta

import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """Load the data from a CSV file and clean it."""
    df = pd.read_csv(file_path)
    df = df.dropna()
    df['Income'] = df['Income'].apply(lambda x: max(x, 0))
    df['Crop_Yield'] = df['Crop_Yield'].apply(lambda x: max(x, 0))
    return df

def simulate_data(output_path):
    """Simulate farmer survey data and save it to CSV."""
    np.random.seed(42)
    data = {
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Income': np.random.normal(5000, 1500, 100),
        'Education': np.random.choice(['Primary', 'Secondary', 'Higher'], 100),
        'ICT_Adoption': np.random.choice([0, 1], 100),
        'Access_to_Water': np.random.choice([0, 1], 100),
        'Subsidies_Received': np.random.choice([0, 1], 100),
        'Crop_Yield': np.random.normal(2000, 300, 100)
    }
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    simulate_data('../data/simulated_farmers_data.csv')
    print('Data simulation complete. Saved to data/simulated_farmers_data.csv')
