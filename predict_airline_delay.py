# Install and Import required librairies
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
import seaborn as sn 
import matplotlib.pyplot as plt


# read the data from Github account
airline_df = pd.read_csv('https://raw.githubusercontent.com/davro76/delay/main/large_dataset_sampled.csv')

# Define a function for each page

# home page function
def home_page():
    # split home page into two same size columns 
    col1, col2 = st.columns(2)
    with col1:
     st.header("About the Author")
     st.write("<p style='color:black; background-color:yellow ;text-align:justify;text-align-last:left;'>Hi,I am Rodney Davermann, a seasoned data analyst with expertise in the domains of economics, agronomics, and statistics. With a background in SQL, Excel, Python, R, machine learning, Tableau, and Power BI, I am well-versed in various data analysis tools and techniques, and I have a strong passion for using data to make informed business decisions, and my expertise in data analysis has helped many organizations to optimize their performance and achieve their goals. With my extensive knowledge in both quantitative and qualitative data analysis, I am an asset to any organization seeking to leverage data to drive growth and success.<p/>", unsafe_allow_html=True)
     #st.write("<p style='color:black;text-align: justify;text-align-last: left;'>Hi,I am Rodney Davermann, a seasoned data analyst with expertise in the domains of economics, agronomics, and statistics. With a background in SQL, Excel, Python, R, machine learning, Tableau, and Power BI, I am well-versed in various data analysis tools and techniques, and I have a strong passion for using data to make informed business decisions, and my expertise in data analysis has helped many organizations to optimize their performance and achieve their goals. With my extensive knowledge in both quantitative and qualitative data analysis, I am an asset to any organization seeking to leverage data to drive growth and success.<p/>",unsafe_allow_html=True)
    
    with col2:
       st.write("Here put App utilities.")


def airline_eda():
   st.write("")
   


def airline_ml():
   st.write('Here is the Neural Network Model to predict Fly delay time')
   




# define the streamlit app pages
PAGES = {
   "Home Page": home_page,
   "Exploratory Data Analysis": airline_eda,
   "Predict Airline Delay Time": airline_ml 
   } 



# Create a Streamlit app
def app():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    app()






