# Bitcoin Price Prediction Project

## Project Overview
This project is designed to predict Bitcoin's price based on multiple data sources such as market indicators, on-chain data, sentiment analysis, and macroeconomic indicators. The goal is to create a machine learning model capable of forecasting Bitcoin's short-term and long-term price movements with high accuracy. This project uses multiple approaches, including Random Forest and deep learning models like LSTM/GRU, to improve the predictive performance of the model.

The project leverages historical Bitcoin price data, external market data, on-chain metrics, and sentiment signals to predict Bitcoin's future price. Additionally, we incorporate models to analyze both short-term (1-7 days) and long-term (30 days) predictions.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Challenges](#challenges)
- [Future Work](#future-work)

## Technologies Used
- **Python**: The programming language used for data manipulation, machine learning, and model building.
- **pandas**: For data cleaning, manipulation, and preprocessing.
- **scikit-learn**: For machine learning model creation and hyperparameter tuning (Random Forest, GridSearchCV).
- **TensorFlow/Keras**: For building deep learning models like LSTM and GRU.
- **Google Colab**: For running the Jupyter notebooks and sharing results.
- **gspread**: For accessing Google Sheets data (e.g., Bitcoin ETF inflows).
- **SQLite**: For storing on-chain and sentiment data in a structured format.
- **Matplotlib**: For data visualization.
- **Google Drive**: For storing datasets and project files.

## Data Sources
1. **Bitcoin Price Data**: Collected from Yahoo Finance via the `yfinance` library. Includes open, close, high, low, volume, etc.
2. **Macroeconomic Indicators**: S&P 500, Nasdaq, Gold, and DXY data were collected for market analysis.
3. **On-Chain Data**: Includes metrics such as Bitcoin's hash rate, exchange inflows, and active addresses (data fetched from Glassnode).
4. **Sentiment Data**: 
   - **Google Trends** data for keywords like "Bitcoin" and "BTC".
   - **Fear & Greed Index** from CNN and Alternative.me for market sentiment analysis.
   - **Twitter Sentiment** (previously replaced by Google Trends).
5. **Bitcoin ETF Inflows/Outflows**: Data sourced from CoinShares or Glassnode, reflecting Bitcoin’s institutional investments.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Bitcoin_Price_Prediction_project.git

pip install -r requirements.txt

## Usage
Open the notebook in Google Colab or Jupyter.
Upload your data to Google Drive if necessary (use the paths as defined in the notebook).
Run the entire notebook in sequence:
Data collection and preprocessing
Feature engineering
Model training (Random Forest, LSTM, GRU)
Evaluation and hyperparameter tuning
Evaluate the models' performance and adjust the features or hyperparameters based on the results.

## Model Evaluation
Random Forest (Short-Term Prediction)

Best Parameters: n_estimators: 500, max_depth: 20, min_samples_split: 5, min_samples_leaf: 4, max_features: 'log2'

Performance:
MAE: 3486.8158
RMSE: 4388.2210
R²: 0.7086


LSTM (Long-Term Prediction)

Training Performance:

MAE: 0.0115
RMSE: 0.0166
R²: 0.9876

Test Performance:
MAE: 0.0428
RMSE: 0.0726
R²: 0.7592


GRU (Long-Term Prediction)

Training Performance:

MAE: 0.0278
RMSE: 0.0363
R²: 0.9410

Test Performance:
MAE: 0.0884
RMSE: 0.1161
R²: 0.3842

## Results
Random Forest outperforms other models in the short-term prediction.
LSTM shows promising results for long-term predictions, with a good R² score of 0.7592 on the test data.
GRU also performs well but with a slightly lower R² score on the test data.

## Challenges
Data Quality: The quality of data (e.g., missing values, inconsistencies) was a key challenge during the feature engineering phase.
Model Overfitting: Hyperparameter tuning was crucial to reduce overfitting, particularly for the Random Forest model.
Data Availability: Some sources, like on-chain metrics or Bitcoin ETF inflows, had incomplete data or required API access.
Hyperparameter Search: Tuning hyperparameters, especially for Random Forest and deep learning models, was computationally expensive and time-consuming.

## Future Work
Deep Learning: Explore additional deep learning models, including more complex architectures like Time-Series Transformers.
Continuous Updates: Set up an automated pipeline to continuously fetch updated data and retrain models.
Advanced Feature Engineering: Integrate more macroeconomic factors such as inflation, interest rates, etc., to improve predictions.
Real-Time Predictions: Implement a real-time prediction system for Bitcoin price using live market data.
