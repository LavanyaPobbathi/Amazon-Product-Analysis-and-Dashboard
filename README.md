# Amazon Product Analysis and Dashboard

<img width="1502" alt="image" src="https://github.com/user-attachments/assets/dc877c1e-6543-413b-b76d-a1eba8571631">


![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Pandas](https://img.shields.io/badge/Pandas-1.4+-orange.svg) ![NumPy](https://img.shields.io/badge/NumPy-Supported-lightblue.svg) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-yellow.svg) ![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-brightgreen.svg) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg) ![Big Data](https://img.shields.io/badge/Big%20Data-Handled-green.svg)


## Overview

This project demonstrates how to handle **large datasets (1.1M+ entries)** effectively, applying **deep data exploration, cleaning, preprocessing, and visualization** techniques. With this project, I have created a end-to-end **data analysis pipelines** and **interactive dashboards**, leveraging **Python, Pandas, Streamlit**, and advanced visualization techniques.

The primary goal of this project is to uncover valuable insights from Amazon's e-commerce dataset, which includes features such as ratings, product categories, prices, and discounts.

**Key Focus Areas:**
- Handling large datasets with 1.1M+ entries and 145 features which is collected from Kaggle website.
- Cleaning and preprocessing data, including outlier detection and feature engineering.
- Developing interactive dashboards for insights visualization using Streamlit.
- Employing advanced statistical and visual techniques for in-depth analysis.

## Build & Dataset Status

### Official Builds

| Dataset Type                 | Status                   | Link/Artifact                    |
|------------------------------|--------------------------|-----------------------------------|
| Full Amazon Dataset (1.1M+)   | ✅ Loaded Successfully    | [Amazon Products Sales Dataset 2023 - Kaggle](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)           |
| CSV Merging (140 CSV files)   | ✅ Merged Successfully    | [merge_df.parquet](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/merge_df.parquet)             |
| Missing Values Imputation     | ✅ Handled Completely     | [Amazon_EDA&Data_Visualization.ipynb](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/Amazon_EDA%26Data_Visualization.ipynb) |
| Outlier Detection & Handling  | ✅ Processed Successfully | [Amazon_EDA&Data_Visualization.ipynb](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/Amazon_EDA%26Data_Visualization.ipynb) |
| Feature Engineering           | ✅ Completed              | [Amazon_EDA&Data_Visualization.ipynb](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/Amazon_EDA%26Data_Visualization.ipynb) |
| Streamlit Dashboard           | ✅ Built Successfully     | [amazon_dashboard.py](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/amazon_dashboard.py)          |


### Artifacts and Resources
- [Dataset Resource Link](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)
- [GitHub Repository](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/tree/main)
- [Dashboard Demo](https://drive.google.com/file/d/1hOZNVJVRCSCJf34RRcweGMhm3v_J9njA/view?usp=sharing)
- [Python Code](https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard/blob/main/Amazon_EDA%26Data_Visualization.ipynb)

## Features
1. **Data Loading and Understanding**:
   - Loaded and merged **140 CSV files** to form a comprehensive dataset.
   - Performed column analysis for common and unique features across product categories.

2. **Data Cleaning and Preprocessing**:
   - Handled missing values with various imputation techniques.
   - Detected and processed outliers in pricing and rating data.
   - Conducted data type conversions and deduplication.

3. **Feature Engineering**:
   - Created derived features like `discount_percentage`, `price_difference`, and `weighted_rating`.
   - Developed interaction terms like `discount_rating_interaction` and `price_rating_interaction` for deeper insights.

4. **Exploratory Data Analysis (EDA)**:
   - Performed univariate, bivariate, and multivariate analysis using visualizations like **box plots, scatter plots, and heatmaps**.
   - Analyzed price distributions, rating trends, and correlations between key product attributes.

5. **Advanced Visualizations**:
   - Built a **correlation heatmap** for numerical features.
   - Created **box plots** and **scatter plots** to uncover relationships between prices, ratings, and categories.
   - Generated word clouds and category-based heatmaps to enhance storytelling.

6. **Insights & Storytelling**:
   - Delivered actionable insights regarding customer satisfaction, discount strategies, and product performance.
   - Identified key product categories for business improvement based on customer feedback and ratings.

7. **Dashboard Creation**:
   - Designed and implemented a **fully interactive dashboard** using Streamlit for **real-time data exploration and visualization**.

## Demo Video

I have recorded a demo video showcasing the **interactive dashboard** in action. The video demonstrates key insights and functionalities of the dashboard, such as filtering by product categories, viewing pricing trends, and analyzing customer ratings.

[Watch the demo video here](https://drive.google.com/file/d/1hOZNVJVRCSCJf34RRcweGMhm3v_J9njA/view?usp=sharing) 

## Dashboard

### Category Analysis 
<img width="1509" alt="image" src="https://github.com/user-attachments/assets/7502f202-f53d-4185-ad60-c7d7d78909cc">

### Price Analysis
<img width="1490" alt="image" src="https://github.com/user-attachments/assets/31eb6ca4-e763-4f3a-90c5-8752f751186b">

### Advanced Visualizations
<img width="1509" alt="image" src="https://github.com/user-attachments/assets/7334873f-e4af-4aef-b0c1-d309b2f33abb">


## Installation

1. **Clone the repository**:
   ```bash
   https://github.com/LavanyaPobbathi/Amazon-Product-Analysis-and-Dashboard.git

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   
3. **Run the Streamlit dashboard**:
   ```bash
   streamlit run amazon_dashboard.py
   

## Technologies Used
  - **Python:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
  - **Streamlit:** Dashboard creation
  - **Data Handling:** Over 1 million records, CSV merging, Parquet and CSV formats for efficient large dataset management
  - **Visualization:** Box plots, scatter plots, heatmaps, word clouds

## Results & Impact
  - Efficiently handled a **massive dataset (1.1M+ rows)**, cleaned, engineered features, and provided meaningful insights.
  - Developed a comprehensive dashboard allowing users to explore the dataset interactively.
  - Uncovered insights about product ratings, price discounts, and customer preferences, potentially guiding business strategies.

## Conclusion
This project will help on how to handle with large datasets for developing data pipelines. I have focused on providing valuable insights through exploratory data analysis, data cleaning, and visualization, complemented by a fully interactive dashboard.


