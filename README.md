# Wind Power Forecasting

## Overview
This project analyses real European wind power generation data to **visualise production trends** and **forecast future output** using an **ARIMA time-series model**.  

## Features
- Reads and processes historical wind generation datasets  
- Generates infographics for hourly, monthly, quarterly, and yearly power output  
- Calculates statistical metrics (mean, standard deviation, skewness)  
- Implements **ARIMA forecasting** to predict future energy generation  
- Automatically adjusts plots and scales for different countries

## Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, Matplotlib, NumPy, SciPy, openpyxl
- **Dataset:** `time_series_60min_singleindex.csv`  

## How to Run
Download the data file and change the placeholder in 'load.py'
   ```bash
   pip install pandas matplotlib numpy scipy, openpyxl
