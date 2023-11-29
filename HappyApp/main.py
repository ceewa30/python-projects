import streamlit as st
import plotly.express as px
import pandas as pd

st.header("In Search for Happiness")
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis", ("GDP","Happiness", "Generosity"))
st.subheader(f"{x_axis} and {y_axis}")

# Load the dataframe
df = pd.read_csv("happy.csv")

match x_axis:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match y_axis:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]


figure = px.scatter(x=x_array, y=y_array, labels={"X": x_axis, "Y": y_axis})
st.plotly_chart(figure)