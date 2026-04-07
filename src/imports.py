# here goes all libraries and modules imports
# standard libraries  
import os
import sys
import time
 
import pandas as pd
import numpy as np 

# visualization
import matplotlib.pyplot as plt
import seaborn as sns

# finance tickers
import yfinance as yf

# import statistics / tests / plots
import statistics
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf, ccf 
from scipy.stats import jarque_bera, norm, t, chi2

# models 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX 
from arch import arch_model
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Darts  
from darts import TimeSeries, concatenate
from sklearn.preprocessing import MinMaxScaler
from darts.dataprocessing.transformers import Scaler, MissingValuesFiller
from darts.models import NBEATSModel 
from darts.utils.callbacks import TFMProgressBar
from darts.metrics import r2_score, mape, mae, rmse, smape 

# ignore warnings
import warnings
warnings.filterwarnings('ignore')