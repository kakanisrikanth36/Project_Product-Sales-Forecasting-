# 📈 Sales Forecasting with Machine Learning & Flask API

## 📝 Problem Statement
Retail businesses often face challenges in anticipating sales fluctuations, especially during holidays, discounts, and across store types. Uncertainty in demand leads to **overstocking** or **stock shortages**, impacting revenue and customer satisfaction.

**Goal:**  
Build a machine learning model that forecasts daily sales based on historical data and integrate it into business operations using a Flask API for real-time predictions.

---

## 🎯 Target Metric
- **Regression Models** → Evaluate performance using:
  - **R² Score** (goodness of fit)
  - **RMSE (Root Mean Squared Error)**
  - **MAE (Mean Absolute Error)**

---

## 🔍 Approach

### 1. **Exploratory Data Analysis (EDA)**
- Analyzed trends in sales by date, store type, region, and holidays
- Checked distribution of sales & outliers
- Identified correlations between features like discounts and order volumes

### 2. **Hypothesis Testing**
- Verified whether holidays and discounts significantly affect sales
- Conducted t-tests/ANOVA on sales grouped by categorical factors

### 3. **Feature Engineering**
- Created lag features and moving averages to capture temporal trends
- Encoded categorical features (store type, discount availability)
- Generated "holiday effect" and "discount effect" features

### 4. **Machine Learning Modeling**
- Trained and compared multiple regression models:
  - **Linear Regression** (baseline)
  - **Ridge/Lasso Regression** (regularization)
  - **XGBoost** (best performing)
- Evaluated models using cross-validation and error metrics

### 5. **Insights & Recommendations**
- **Discounts** strongly boost sales, but excessive discounting lowers profitability → optimize frequency
- **Holidays** cause spikes in demand → plan stock allocation accordingly
- **Store Type & Region** differences suggest customized inventory strategies

---

## 🏆 Final Results
- **Best Model:** XGBoost
- **R² Score:** ~0.85
- **RMSE:** Reduced by ~20% vs baseline Linear Regression
- **MAE:** Indicates average forecast error of ~3–5% of daily sales

---

## 🚀 Deployment

### Steps Taken
1. **Model Serialization** – Trained XGBoost model saved using `joblib` (`model.pkl`)
2. **Flask API Development** – Built REST API (`app.py`) with endpoints:
   - `/` → Health check
   - `/predict` → Returns sales forecast for given inputs
3. **Testing** – Created `test_api.py` to send JSON requests and verify predictions
4. **Containerization/Hosting (Optional)** – Can be deployed to **Render/Railway/Heroku** for public use
5. **Integration** – API can be connected to dashboards (e.g., Tableau, Power BI) for real-time business insights

---

## 📦 Example API Request & Response

**Request**
```json
{
  "Store_id": 1,
  "Holiday": 0,
  "Discount": "Yes",
  "Sales": 2500,
  "Orders": 300
}
```

**Response**
```json
{"prediction": [2750.43]}
```

---

## 🙌 Author
**Popatsing Waghela**  
Aspirant Data Scientist | Finance & Procurement Analytics | Machine Learning Enthusiast
