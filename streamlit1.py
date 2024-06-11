import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello world")
st.subheader("Hi, I am YQ")
st.header("I am header")
st.text_input("Hi I am text function")

chart_data = pd.DataFrame(np.random.randn(20, 3))
columns = ["a", "b", "c"]
st.line_chart(chart_data)

#st.pyplot
arr = np.random.normal(1, 1, size = 100)
fig, ax = plt.subplots()
ax.hist(arr, bins = 20)

st.pyplot(fig)

#st.map
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(df)

st.markdown("# main page")
st.write("# main page")

option = st.selectbox("What ice-cream flavour do you like the most",
                ["Blueberry", "Mango", "Grapes", "Raspberry"]
)

#st.tabs
from datetime import datetime
st.write(datetime(2020, 1, 10, 10, 30))

import pytz
st.write(datetime(2020, 1, 10, 10, 30))