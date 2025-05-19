
# regression_analysis.py
# Author: Yetta

import pandas as pd
import statsmodels.api as sm

def perform_regression(df):
    """Perform OLS regression analysis."""
    X = sm.add_constant(df[['Income', 'ICT_Adoption', 'Subsidies_Received']])
    Y = df['Crop_Yield']
    model = sm.OLS(Y, X).fit()
    return model

def print_summary(model):
    """Print the summary of the regression model."""
    print(model.summary())

if __name__ == "__main__":
    df = pd.read_csv('../data/simulated_farmers_data.csv')
    model = perform_regression(df)
    print_summary(model)
