# Install and Import required librairies
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam



# load the data
airline_data = pd.read_csv('https://raw.githubusercontent.com/davro76/delay/main/large_dataset_sampled.csv')

# drop date feature
airline_data1 = airline_data.drop('date', axis=1)



def main():
    # page configuration
    st.set_page_config( layout = 'wide', initial_sidebar_state='expanded', page_title='Predict Fly Delay.')

    # define and customize the sidebar
    st.sidebar.markdown("<h1 style ='color:black; blackgroundcolour:green; text-align:center;font-weight:bold;font-family: Comic Sans MS'>Navigate Through<h1/>", unsafe_allow_html=True)
    pages = st.sidebar.radio("",['Home', 'EDA', 'Predicting Fly Delay']) # sidebar caption and option

    # if else statement for pages navigation
    if pages == 'Home':
        home()

    elif pages == 'EDA':
        airline_eda()

    elif pages == 'Predicting Fly Delay':
        predict_airline_delay()


# home page function
def home():
    # split home page into two same size columns 
    col1, col2 = st.columns(2)
    with col1:
     st.header("About the Author")
     st.write("<p style='color:black; background-color:yellow ;text-align:justify;text-align-last:left;'>Hi,I am Rodney Davermann, a seasoned data analyst with expertise in the domains of economics, agronomics, and statistics. With a background in SQL, Excel, Python, R, machine learning, Tableau, and Power BI, I am well-versed in various data analysis tools and techniques, and I have a strong passion for using data to make informed business decisions, and my expertise in data analysis has helped many organizations to optimize their performance and achieve their goals. With my extensive knowledge in both quantitative and qualitative data analysis, I am an asset to any organization seeking to leverage data to drive growth and success.<p/>", unsafe_allow_html=True)
    
    with col2:
        st.write('''## Purpose of this App
    This app could be use to:
    1. Visualize airline delays data all around United States.
     2. Predict either a fly will delay or not by using a Neural Network Model.''')


def airline_eda():
    st.header('Exploratory Data Analysis') # page title

     # display some rows of the dataset
    st.markdown("<h2 style ='color:red; text-align:center;font-family:Comic Sans MS;'>Airline Fly Delay Data<h2/>", unsafe_allow_html= True)
    datum = airline_data1.head(3)
    st.write(datum)

    # summary statistic for numeric features of the dataset and pivot table for categorical features

    st.markdown("<h2 style ='color:red;text-align:center;font-family:Comic Sans MS;'>Descriptive Statistics<h/>", unsafe_allow_html = True) # customize header 2
 # split airline_data into categorical and numerical features
    objects = ['object']
    Cat =  airline_data1.select_dtypes(include=objects)
    Cat2 = Cat.drop(['dep_airport', 'arr_airport','route','mkt_ccode'], axis=1)
    #Cat1 = Cat.head(2)

    # numerical features statistics
    Num = airline_data1.select_dtypes(exclude=objects).drop('delay', axis=1)
    stats = Num.describe()
    st.write(stats)

    # pivot table for categorical features
    st.markdown("<h3 style ='color:red;text-align:center;font-family:Comic Sans MS;'>Pivot Tables for Categorical Features<h3/>", unsafe_allow_html=True)

    pivot_columns = []
    for col in Cat2.columns:
        if Cat2[col].nunique() > 1:  # Check if the column has more than 1 unique value
            pivot_cat = Cat2.groupby(col).size().reset_index(name='count')
            pivot_columns.append((col, pivot_cat))

    num_cols = len(pivot_columns)
    cols = st.columns(num_cols)
    for i in range(num_cols):
        col_name, pivot_table = pivot_columns[i]
        with cols[i]:
            st.write(f"Pivot Table for {col_name}:")
            st.write(pivot_table)
    if num_cols == 0:
        st.write("No categorical columns with more than one unique value found.")

    # Charts
    st.markdown("<h1 style = 'color:red;text-align:center;font-family:Comic Sans MS;'>Charts<h1/>", unsafe_allow_html=True)

    st.markdown("<p style ='color:brown;text-align:center;font-weight:bold;font-family: Comic Sans MS;'>Which routes are most prone to delays?<p/>", unsafe_allow_html=True)

    df = airline_data1.groupby('route')['arr_delay_time_actual'].mean().reset_index().round(3)  # grouping by route
    df_sorted = df.sort_values(by='arr_delay_time_actual', ascending=False).head(10)

    st.write(df_sorted)

def predict_airline_delay():
    st.title('Will You Arrive On Time?')

    
# Create a Streamlit app
#def main():
    #home_page()

if __name__ == "__main__":
    main()

 

