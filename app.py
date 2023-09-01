import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    df = pd.read_csv('google_stock_price.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Plot line chart
def plot_line_chart(df, start_date, end_date):
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    plt.figure(figsize=(12,6))
    plt.plot(df['Date'], df['Close'])
    plt.title('Google Stock Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    st.pyplot()

# Plot histogram
def plot_histogram(df):
    plt.figure(figsize=(12,6))
    plt.hist(df['Volume'], bins=30, alpha=0.75)
    plt.title('Histogram of Volume of Stocks Traded')
    plt.xlabel('Volume')
    plt.ylabel('Frequency')
    st.pyplot()

# Display statistics
def display_statistics(df):
    st.write(df.describe())

def main():
    df = load_data()

    st.title('Google Stock Price Analysis')

    start_date = st.date_input('Start date', df['Date'].min())
    end_date = st.date_input('End date', df['Date'].max())

    if start_date > end_date:
        st.error('Error: End date must fall after start date.')
    else:
        plot_line_chart(df, start_date, end_date)
        plot_histogram(df)
        display_statistics(df)

if __name__ == "__main__":
    main()
