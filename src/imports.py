# here goes all libraries and modules imports
# standard libraries 
import os 
import time
import pytz
from datetime import datetime 

import pandas as pd
import numpy as np
import math

# finance tickers
import yfinance as yf

# visualization
import matplotlib.pyplot as plt
import seaborn as sns

# stats / tests / plots
import statistics
from scipy.stats import jarque_bera
from statsmodels.stats.diagnostic import acorr_ljungbox, het_arch
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf, ccf 
from scipy.stats import norm, t, chi2

# models
# import pmdarima as pm
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
# from pmdarima.arima import auto_arima
from arch import arch_model

# Darts  
from sklearn.preprocessing import MinMaxScaler
from darts.models import NBEATSModel
from darts.dataprocessing.transformers import Scaler 
from darts.metrics import r2_score, mape, mae, rmse, smape
from darts.dataprocessing.transformers import MissingValuesFiller
from darts.utils.callbacks import TFMProgressBar
from darts import TimeSeries, concatenate

# ignore warnings
import warnings
warnings.filterwarnings('ignore')