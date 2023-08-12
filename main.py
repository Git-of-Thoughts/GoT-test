import streamlit as st
from dca_strategy import DCA_Strategy
from sensitivity_analysis import Sensitivity_Analysis
from visualizer import Visualizer
from asset import Asset

def main():
    st.title('Dollar Cost Averaging Backtester')

    # User inputs
    asset_name = st.text_input('Enter the name of the asset:')
    start_date = st.date_input('Enter the start date of the investment period:')
    end_date = st.date_input('Enter the end date of the investment period:')
    investment_amount = st.number_input('Enter the amount of each investment:')
    investment_frequency = st.selectbox('Select the frequency of investment:', ['Daily', 'Weekly', 'Monthly'])

    # Fetch asset data
    asset = Asset(asset_name)
    asset.fetch_data(start_date, end_date)

    # Calculate DCA strategy return
    dca_strategy = DCA_Strategy(asset, investment_amount, investment_frequency)
    dca_return = dca_strategy.calculate_return()

    # Perform sensitivity analysis
    sensitivity_analysis = Sensitivity_Analysis(dca_strategy)
    sensitivity_results = sensitivity_analysis.perform()

    # Visualize results
    visualizer = Visualizer()
    visualizer.plot_dca_return(dca_return)
    visualizer.plot_sensitivity_results(sensitivity_results)

if __name__ == '__main__':
    main()
