# Amazon Product Analysis and Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) 
![Pandas](https://img.shields.io/badge/Pandas-1.4+-orange.svg) 
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg) 
![Big Data](https://img.shields.io/badge/Big%20Data-Handled-green.svg) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-blue.svg) 
![NumPy](https://img.shields.io/badge/NumPy-1.21+-orange.svg) 
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-blue.svg) 
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)

## Overview

This project demonstrates my ability to handle **large datasets (1.1M+ entries)** effectively. Through **data exploration, cleaning, preprocessing, and visualization**, I've created a **Streamlit dashboard** for dynamic analysis. The project uses **Python**, **Pandas**, and **Streamlit** to provide insights from an e-commerce dataset that includes features like product ratings, categories, prices, and discounts.

**Key Focus Areas:**
- Working with large datasets (1.1M+ entries and 145 features).
- Data cleaning and feature engineering for deep insights.
- Interactive dashboard creation using **Streamlit**.
- Advanced visualization techniques for storytelling and exploration.

## Build & Dataset Status

### Official Builds

| Dataset Type                 | Status                   | Link/Artifact                    |
|------------------------------|--------------------------|-----------------------------------|
| Full Amazon Dataset (1.1M+)   | ✅ Loaded Successfully    | [amazon_data folder](#)           |
| CSV Merging (140 CSV files)   | ✅ Merged Successfully    | [merge_df.parquet](#)             |
| Missing Values Imputation     | ✅ Handled Completely     | [Amazon_EDA&Data_Visualization.ipynb](#) |
| Outlier Detection & Handling  | ✅ Processed Successfully | [Amazon_EDA&Data_Visualization.ipynb](#) |
| Feature Engineering           | ✅ Completed              | [Amazon_EDA&Data_Visualization.ipynb](#) |
| Streamlit Dashboard           | ✅ Built Successfully     | [amazon_dashboard.py](#)          |

### Artifacts and Resources
- [GitHub Repository](#)
- [Project Documentation](#)
- [Dashboard Demo](video2751251323.mp4)
- [Full Report & Insights](Amazon_EDA&Data_Visualization.ipynb)

## Features
1. **Data Loading and Understanding**:
   - Loaded and merged **140 CSV files** into a **Parquet** file (`merge_df.parquet`) for efficient handling.
   - Analyzed and inspected the dataset structure, identified common and unique columns.

2. **Data Cleaning and Preprocessing**:
   - Handled missing values and outliers using imputation and advanced preprocessing techniques.
   - Converted data types for consistency and removed duplicates.

3. **Feature Engineering**:
   - Created derived features like `discount_percentage`, `price_difference`, and `weighted_rating`.
   - Developed interaction terms such as `discount_rating_interaction` and `price_rating_interaction`.

4. **Exploratory Data Analysis (EDA)**:
   - Conducted univariate, bivariate, and multivariate analysis using various visualizations (scatter plots, heatmaps, etc.).
   - Analyzed relationships between key variables like prices, ratings, and categories.

5. **Advanced Visualizations**:
   - Used **Seaborn** and **Matplotlib** to build box plots, scatter plots, and heatmaps.
   - Created word clouds for text-based insights and heatmaps for category-based ratings analysis.

6. **Insights & Storytelling**:
   - Provided actionable insights on customer satisfaction, discount strategies, and product performance.
   - Identified product categories that could benefit from further improvement based on ratings and feedback.

7. **Dashboard Creation**:
   - Implemented an interactive dashboard using **Streamlit** to allow real-time data exploration and analysis.

## Demo Video

Watch the recorded demo video showcasing the interactive dashboard:
[Watch the demo video here](video2751251323.mp4)

The demo illustrates how to filter product categories, visualize pricing trends, and analyze customer ratings.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/amazon-dataset-eda-dashboard.git

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit dashboard**:
  ```bash
  streamlit run amazon_dashboard.py
  ```

## Technologies Used
  - **Python:** Pandas, NumPy, Matplotlib, Seaborn
  - **Streamlit:** For creating interactive dashboards
  - **Data Handling:** Parquet and CSV formats for efficient large dataset management
  - **Visualization:** Box plots, scatter plots, heatmaps, word clouds

## Results & Impact
  - Successfully processed and analyzed a massive dataset (1.1M+ rows).
  - Created an interactive dashboard enabling users to explore insights from the dataset.
  - Extracted key insights regarding product pricing, customer satisfaction, and discount strategies.

## Conclusion
This project demonstrates my proficiency in working with large datasets and developing data pipelines. I have focused on providing valuable insights through exploratory data analysis, data cleaning, and visualization, complemented by a fully interactive dashboard.


### Key Changes:
1. **Filenames**: Updated to match the actual files from your project (e.g., `amazon_dashboard.py`, `Amazon_EDA&Data_Visualization.ipynb`, `merge_df.parquet`, `video2751251323.mp4`).
2. **Demo Video**: The demo video section now links directly to your provided video file (`demo.mp4`).
3. **Data Files**: The `merge_df.parquet` file is referenced as your merged dataset, and the notebook file (`Amazon_EDA&Data_Visualization.ipynb`) for the EDA process.

You can further customize the links and paths in this README once you upload the repository to GitHub. Let me know if you'd like to adjust anything further!

