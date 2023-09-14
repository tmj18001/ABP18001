import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Simple Streamlit App')

st.sidebar.header('Parameters')
x_max = st.sidebar.slider('x max value', 0, 100, 50)
num_points = st.sidebar.slider('Number of points', 0, 1000, 500)

x = np.linspace(0, x_max, num_points)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Sine Wave')

st.pyplot(plt)
