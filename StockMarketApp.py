# Description : This is a stock market dashboard to show some charts and data on few stocks

# importing libraries
import streamlit as st
import pandas as pd
from PIL import Image

# Adding a title and an Image
st.write("""
# Stock Market Web Application
**Visually** shows the data on a stock!
Date range from Aug 12 , 2019 to Aug 10, 2020
""")

image = Image.open(
    "C:\PycharmProjects\Stock Market Web App\imgs\stock-exchange-3087396_1920.jpg")
st.image(image, use_column_width=True)

# Creating a Sidebar
st.sidebar.header('User Input')


# Creating a function to get the users input

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2019-08-12")
    end_date = st.sidebar.text_input("End Date", "2020-08-10")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol


# Creating function to get company name


def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    if symbol == 'AAPL':
        return 'Apple'
    if symbol == 'FB':
        return 'Facebook'
    if symbol == 'GOOGL':
        return 'Google'
    if symbol == 'MSFT':
        return 'Microsoft'
    if symbol == 'NFLX':
        return 'Netflix'
    if symbol == 'TM':
        return 'Toyota Motors'
    if symbol == 'TSLA':
        return 'Tesla'
    else:
        'NONE'

# Create a  function to get company data and timeframe


def get_data(symbol, start, end):

    # load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/AMZN.csv")
    if symbol.upper() == 'AAPL':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/AAPL.csv")
    if symbol.upper() == 'FB':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/FB.csv")
    if symbol.upper() == 'GOOGL':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/GOOGL.csv")
    if symbol.upper() == 'TM':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/TM.csv")
    if symbol.upper() == 'TSLA':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/TSLA.csv")
    if symbol.upper() == 'MSFT':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/MSFT.csv")
    elif symbol.upper() == 'NFLX':
        df = pd.read_csv(
            "C:/PycharmProjects/Stock Market Web App/Stocks/NFLX.csv")
    # else:
    #     df = pd.DataFrame(
    #         columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])

    # Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # Start the data from the top of the data
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    # Start the data from the bottom of the data
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break

    # Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row+1, :]


# Get  the user input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
# Get the company name
company_name = get_company_name(symbol.upper())


# Giving symboland stock name
st.sidebar.text("Symbols and company name")
st.sidebar.text("AMZN   Amazon")
st.sidebar.text("TSLA   Tesla")
st.sidebar.text("MSFT   Microsoft")
st.sidebar.text("FB     Facebook")
st.sidebar.text("TM     Toyota Motors")
st.sidebar.text("GOOGL  Google")
st.sidebar.text("AAPL   Apple")
st.sidebar.text("NFLX   Netflix")

# display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

# display the volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

# get the statistics
st.header('Data Statistics')
st.write(df.describe())
