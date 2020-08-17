import platform 
print('Python version = ' + platform.python_version())
import yfinance as yf
print('yfinance version = ' + yf.__version__)

import pandas as pd

tesla = yf.Ticker('TSLA')

print(tesla.info["sharesShortPriorMonth"])
