# README

Project Title

Brief Project Overview
 blah blah blah

Project Objectives
The main objectives of this project are:

    Collect and preprocess financial time series data:
        Retrieve Forex price data using the yfinance Python library
        Compute log returns 

    Perform Exploratory Data analysis
        Visual and quatitatve analysis
            Returns distribution
            Autocorrelation
            Heteroskedasticity 
        
    Implement econometric volatility models
        Estimate a GARCH(1,1) model
        Generate volatility forecasts

    Implement deep learning forecasting models
        Train an N-BEATS neural network
        Forecast volatility using past observations

    Compare forecasting performance
        Evaluate model accuracy using:
            RMSE (Root Mean Squared Error)
            sMAPE (Symmetric Mean Absolute Percentage Error)

    Analyze results
        Compare predictive accuracy
        Discuss advantages and limitations of both approaches


Repository structure
FINAL PROJECT
    data/                               <- Raw and processed financial datasets
    notebooks/                          <- Jupyter notebooks used for analysis and experimentation
        01_forex_data_analysis.ipynb    <- Exploratory analysis of Forex data
        02_garch_model.ipynb            <- Implementation and estimation of GARCH models
        03_nbeats_model.ipynb           <- Training and evaluation of N-BEATS deep learning model
        04_model_comparison.ipynb       <- Forecast comparison and performance evaluation
    reports/                            <- Literature and project documentation
        rapport.pdf
    results/                            <- Outputs generated during the project
        figures/                        <- Plots and visualization of results
        forecasts/                      <- Model predictions
    tables/                             <- Performance comparison tables
    src/
        imports.py                      <- Project libraries
    utils.py                            <- Helper functions
    README.txt