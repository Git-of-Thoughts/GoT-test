import pandas as pd
import yfinance as yf

class Asset:
    def __init__(self, name):
        self.name = name
        self.data = None

    def fetch_data(self, start_date, end_date):
        self.data = yf.download(self.name, start=start_date, end=end_date)
