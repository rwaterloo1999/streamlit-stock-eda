import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Price Histogram Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

st.subheader("Data Preview")
st.write(df.head())

st.sidebar.header("Inputs")

# Filter by stock symbol (makes chart meaningful)
symbols = sorted(df["symbol"].unique())
selected_symbol = st.sidebar.selectbox("Select Stock", symbols)

df_filtered = df[df["symbol"] == selected_symbol]

# Select numeric variable
numeric_columns = df_filtered.select_dtypes("number").columns
selected_var = st.sidebar.selectbox("Select Variable", numeric_columns)

# Default bins = 50
bins = st.sidebar.slider("Number of Bins", 5, 100, 50)

# Prepare data
x = df_filtered[selected_var].dropna()

# Plot
fig, ax = plt.subplots()
ax.hist(x, bins=bins)
ax.set_title(f"{selected_symbol}: Distribution of {selected_var}")
ax.set_xlabel(selected_var)
ax.set_ylabel("Frequency")

st.pyplot(fig)

# Summary statistics
st.subheader("Summary Statistics")
st.write(x.describe())
