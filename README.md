# 📈 Bitcoin Price Predictor

## 🚀 Project Overview
This project focuses on forecasting Bitcoin prices using machine learning. By combining technical indicators, macroeconomic data, and on-chain metrics, we built a two-model system:

- **Random Forest** for short-term predictions (1–7 days)
- **GRU (Gated Recurrent Unit)** for long-term forecasts (30+ days)

The project is implemented in Python and designed to evolve into a user-facing application using Streamlit.

---

## 📂 Repository Structure
bitcoin-price-predictor-app/
├── notebooks/
   ├── 01_data_collection_and_feature_engineering.ipynb
   ├── 02_data_preprocessing_and_split.ipynb 
   │── 03_model_training_and_evaluation.ipynb 
├── models/
   ├── rf_model_v1.pkl
   ├── gru_model_v1.keras
   │── feature_scaler.pkl
   │── target_scaler.pkl 
├── data/
   ├── preprocessed_data/
   │── raw/ 
├── results/ 
├── bitcoin_app.py 
├── README.md
├── requirements.txt

## 🔧 Technologies Used

| Tool                       | Purpose                                    |
|----------------------------|--------------------------------------------|
| **Python, pandas**         | Data wrangling and manipulation            |
| **scikit-learn**           | Random Forest + preprocessing + evaluation |
| **TensorFlow / Keras**     | GRU model for long-term forecasting        |
| **Google Colab**           | Notebook development                       |
| **Streamlit**              | Front-end interface for predictions (WIP)  |
| **Google Drive + gspread** | Dataset storage + ETF flow updates         |
| **SQLite**                 | On-chain and sentiment database            |
| **Plotly / Matplotlib**    | Visualization                              |

## 📊 Data Sources

- **Bitcoin Prices**: Yahoo Finance (`yfinance`)
- **Macro Assets**: S&P 500, Nasdaq, Gold, DXY
- **On-Chain Data**: Hash rate, exchange flows, MVRV, active addresses
- **Sentiment Data**: 
  - Google Trends
  - Fear & Greed Index (Alt.me & CNN)
- **ETF Flows**: Manually updated from CoinShares via Google Sheets

---

## ▶️ How to Run

1. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/Marc-Seger/bitcoin-price-predictor-app.git
   cd bitcoin-price-predictor-app
   pip install -r requirements.txt

2. Run the notebooks:
   01_data_collection_and_feature_engineering.ipynb
   02_data_preprocessing_and_split.ipynb
   03_model_training_and_evaluation.ipynb

3. Launch the app (coming soon):
   streamlit run bitcoin_app.py

## ✅ Model Performance (mockup results)

📉 Random Forest (Short-Term)
R²: 0.71
MAE: $3,487
RMSE: $4,388

📈 GRU (Long-Term)
Train R²: 0.99 | Test R²: 0.76
MAE: 0.0428 (test)
RMSE: 0.0726 (test)

## 📌 Key Learnings

Simulating future features (VWAP, EMA, lagged price) was crucial for long-term predictions.
Recursive prediction strategy was implemented for horizon-based accuracy.
Feature selection played a major role in reducing overfitting and improving generalization.

## 🧩 Challenges

⚠️ Handling missing and incomplete on-chain data
🔄 Keeping data up to date for training (manual ETF updates)
🧠 Balancing short-term volatility with long-term trend recognition
💻 Time-intensive model tuning (especially for deep learning)

## 🛠️ Future Work

Improve long-term GRU model (v2) with better regularization
Develop a dedicated Streamlit predictor interface
Add real-time pipeline with automatic retraining
Integrate advanced macro factors (inflation, interest rates, money supply)

## 📁 Related Projects

Bitcoin & Assets Dashboard
Power BI Dashboard (Coming Soon)
Portfolio Website

🧠 Built with passion by Marc Seger – [Linkedin](https://www.linkedin.com/in/marc-seger/) . [GitHub](https://github.com/Marc-Seger)