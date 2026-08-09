# ferry-pulse-ai
Short-Term Ferry Ticket Demand Forecasting and Predictive Decision Support System using Machine Learning
# Ferry Pulse AI

## Short-Term Ferry Ticket Demand Forecasting and Predictive Decision Support System using Machine Learning

Ferry Pulse AI is a machine-learning-based forecasting and predictive decision support system designed to forecast short-term ferry ticket demand and support operational planning.

The system analyzes timestamped ferry ticket sales and redemption data, creates time-based and demand-based features, compares multiple machine learning models, forecasts demand at multiple future horizons, detects potential demand spikes, estimates forecast uncertainty, and provides operational recommendations.

---

## Project Overview

Ferry transportation systems need reliable short-term demand forecasts to support operational planning and prepare for periods of high passenger demand.

This project develops a machine learning pipeline that uses historical ferry ticket demand data to:

- Forecast short-term ferry ticket demand
- Compare multiple machine learning algorithms
- Predict demand for multiple future time horizons
- Detect potential demand spikes
- Measure demand pressure
- Estimate forecast uncertainty
- Generate operational recommendations
- Export trained models and forecasting results

---

## Key Features

### 1. Data Loading and Exploration

The notebook loads a CSV dataset containing timestamped ferry ticket information.

The data is examined for:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Duplicate records
- Timestamp ranges
- Time gaps between observations

---

### 2. Demand Feature Engineering

The system creates demand-related features including:

- Total Demand
- Sales and Redemption Gap
- Redemption Ratio
- Demand per Ticket Type
- Demand momentum
- Demand acceleration
- Demand volatility
- Historical time-based demand

The primary demand variable is calculated from:

```text
Total Demand = Sales Count + Redemption Count
