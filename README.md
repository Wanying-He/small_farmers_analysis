
# Small Farmers Analysis

## Project Overview
This project focuses on analyzing the welfare and productivity of small farmers based on survey data. It includes data simulation, data cleaning, statistical analysis using OLS regression, and visualization to understand the impact of various factors such as income, ICT adoption, and government subsidies on crop yield.

## Project Structure
```
small_farmers_analysis/
│
├── README.md                    # Project description and usage
├── requirements.txt             # Dependencies for Python environment
├── data/                        # Placeholder for raw and processed data
│   └── simulated_farmers_data.csv
│
├── src/                         # Source code
│   ├── data_preprocessing.py    # Data cleaning and preprocessing logic
│   ├── regression_analysis.py   # OLS regression model implementation
│   └── visualization.py         # Plot generation and visualization
│
└── main.py                      # Main script to execute the analysis pipeline
```

## Installation
```
pip install -r requirements.txt
```

## Usage
To run the full analysis pipeline:
```
python main.py
```

## Data Description
The project uses simulated survey data with the following columns:
- Region
- Income
- Education
- ICT_Adoption
- Access_to_Water
- Subsidies_Received
- Crop_Yield

## Analysis Steps
1. **Data Preprocessing**
2. **Regression Analysis**
3. **Visualization of Regional Distributions**

## Results
- The analysis identifies key factors impacting crop yield in different regions.
- ICT adoption and government subsidies have been identified as significant predictors of yield improvements.

## License
MIT License
