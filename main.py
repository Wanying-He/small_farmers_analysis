
# main.py
# Author: Yetta

from data_preprocessing import load_and_clean_data, simulate_data
from regression_analysis import perform_regression, print_summary
from visualization import plot_yield_by_region, plot_ict_vs_yield

# Step 1: Simulate Data and Save to CSV
print("[INFO] Simulating data...")
simulate_data('./simulated_farmers_data.csv')
print("[INFO] Data simulation complete.")

# Step 2: Load and Clean Data
print("[INFO] Loading and cleaning data...")
data = load_and_clean_data('./simulated_farmers_data.csv')
print("[INFO] Data loaded and cleaned.")

# Step 3: Perform Regression Analysis
print("[INFO] Performing regression analysis...")
model = perform_regression(data)
print_summary(model)

# Step 4: Generate Visualizations
print("[INFO] Generating visualizations...")
plot_yield_by_region(data)
plot_ict_vs_yield(data)

print("[INFO] Analysis complete.")
