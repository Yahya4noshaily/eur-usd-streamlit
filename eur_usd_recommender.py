import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import requests

st.set_page_config(page_title="EUR/USD توصيات", layout="wide")
st.title("📈 توصيات حية على EUR/USD")
data = yf.download("EURUSD=X", period="5d", interval="30m")

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
))
fig.update_layout(title="شارت مباشر EUR/USD", xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

st.subheader("📌 توصية حية:")
st.info("✅ شراء عند 1.0860 | وقف خسارة: 1.0825 | هدف: 1.0910")
