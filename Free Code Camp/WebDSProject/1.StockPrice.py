import yfinance as yf
import streamlit as st
from datetime import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta


st.write("""
    # Simple Stock Price App 

    Shown are the Shown are the stock ***Closing Price*** and ***Volume*** of Google!
""")

today_date = datetime.today().strftime('%Y-%m-%d')
ten_years_ago_date = datetime.now() - relativedelta(years=3)


# it's like abbr for place where we will take data from
tickerSymbol = 'GOOGL'
# Getting Data
Data = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = Data.history(period='1d', start=ten_years_ago_date, end= today_date)

st.write("""
    ## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
    ## Volume Price
""")
st.line_chart(tickerDf.Volume)