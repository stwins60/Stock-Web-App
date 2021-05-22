import json

import requests
import streamlit as st
import yfinance as yf
import FinNews as fn
import config
from datetime import date

def main():
    st.title('STOCK APP')

    menu = ["Stock", "Cypto Exchange"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Stock":
        st.subheader('Welcome to Stock Page')

        sym = st.text_input('Enter the company ticker')
        st.text('eg: aapl, amzn, hpq, etc.')

        if st.button('Search'):

            data = yf.Ticker(sym)
            datalist = data.get_info()
            st.image(datalist['logo_url'])
            st.text('NAME: ' + datalist['longName'])
            st.text('WEBSITE: ' + datalist['website'])
                # st.markdown('BUSINESS SUMMARY: ' + dt['longBusinessSummary'])
            st.text('Sector: ' + datalist['sector'])
            st.text('Quote Type: ' + datalist['quoteType'])
            st.text('INDUSTRY: ' + datalist['industry'])
            st.text('CURRENCY: ' + datalist['currency'])
            st.text('ANNUAL DIVIDEND YIELD: ' + str(datalist['trailingAnnualDividendYield']))
            st.text('MARKET OPEN: ' + str(datalist['regularMarketOpen']))
            st.text('Quote Type: ' + datalist['quoteType'])
            st.text('INDUSTRY: ' + datalist['industry'])
            st.text('PREVIOUS CLOSE: ' + str(datalist['previousClose']))
            st.text('HIGH: ' + str(datalist['regularMarketDayHigh']))
            st.text('OPEN: ' + str(datalist['open']))
            st.text('REGULAR MARKET PRICE: ' + str(datalist['regularMarketPrice']))
            st.text('DIVIDEND RATE: ' + str(datalist['dividendRate']))
            st.text('MARKET VOLUME: ' + str(datalist['regularMarketVolume']))
            st.text('BID SIZE: ' + str(datalist['bidSize']))
            st.text('BID: ' + str(datalist['bid']))
            st.text('VOLUME: ' + str(datalist['volume']))
            st.text('AVERAGE VOLUME: ' + str(datalist['averageVolume']))
            st.text('LAST UPDATE: ' + str(date.today()))

    elif choice == 'Cypto Exchange':
        st.subheader('Welcome to Cypto Exchange rate')
        cypto = st.text_input('Enter the cryptocurrency you want to convert from')
        currency = st.text_input('Enter the currency you want to convert to')

        if st.button('Convert'):
            url = "https://alpha-vantage.p.rapidapi.com/query"

            querystring = {"from_currency": {cypto}, "function": "CURRENCY_EXCHANGE_RATE", "to_currency": {currency}}

            headers = {
                'x-rapidapi-key': config.API_KEY,
                'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            cypto_data = response.text
            data = json.loads(cypto_data)
            for i in data:
                dt = data[i]
                # st.text(dt)

            st.text('NAME: ' + dt['2. From_Currency Name'])
            st.text('SYMBOL: ' + dt['1. From_Currency Code'])
            st.text('CURRENCY NAME: ' + dt['4. To_Currency Name'])
            st.text('CURRENCY CODE: ' + dt['3. To_Currency Code'])
            st.text('EXCHANGE RATE: ' + str(dt['5. Exchange Rate']))
            st.text('TIME ZONE: ' + dt['7. Time Zone'])
            st.text('ASK PRICE: ' + str(dt['9. Ask Price']))
            st.text('BID PRICE: ' + str(dt['8. Bid Price']))
            st.text('LAST REFRESHED: ' + str(dt['6. Last Refreshed']))


if __name__ == '__main__':
    main()
