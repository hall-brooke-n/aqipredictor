### KICKOFF - CODING AN APP IN STREAMLIT

#conda install -c conda-forge streamlit

### import libraries
import pandas as pd
import streamlit as st
import joblib

st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
    This is is just a very small window into its capabilities.')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



#######################################################################################################################################
### Create a title

st.title("Kickoff - Live coding an app")

# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
### DATA LOADING

### A. define function to load data
@st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path, num_rows):

    df = pd.read_csv(path, nrows=num_rows)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

    df = df.rename(columns={'Start Station Latitude': 'lat', 'Start Station Longitude': 'lon'})     
    df['Start Time'] = pd.to_datetime(df['Start Time'])      # reset dtype for column
     
    return df

### B. Load first 50K rows
df = load_data("NYC_bikes_small.csv", 50000)

### C. Display the dataframe in the app
st.dataframe(df)


#######################################################################################################################################
### STATION MAP

st.subheader('Location Map - NYC bike stations')      

st.map(df)   


#######################################################################################################################################
### DATA ANALYSIS & VISUALIZATION

### B. Add filter on side bar after initial bar chart constructed

st.sidebar.subheader("Usage filters")
round_trip = st.sidebar.checkbox('Round trips only')

if round_trip:
    df = df[df['Start Station ID'] == df['End Station ID']]


### A. Add a bar chart of usage per hour

st.subheader("Daily usage per hour")

counts = df["Start Time"].dt.hour.value_counts()
st.bar_chart(counts)


### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
#### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
#### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
#### Automating processes and handling real-time data


#######################################################################################################################################
### MODEL INFERENCE

st.subheader("Using pretrained models with user input")

# A. Load the model using joblib
model = joblib.load('sentiment_pipeline.pkl')

# B. Set up input field
text = st.text_input('Enter your review text below', 'Best. Restaurant. Ever.')

# C. Use the model to predict sentiment & write result
prediction = model.predict({text})

if prediction == 1:
    st.write('We predict that this is a positive review!')
else:
    st.write('We predict that this is a negative review!')



#######################################################################################################################################
### Streamlit Advantages and Disadvantages
    
st.subheader("Streamlit Advantages and Disadvantages")
st.write('**Advantages**')
st.write(' - Easy, Intuitive, Pythonic')
st.write(' - Free!')
st.write(' - Requires no knowledge of front end languages')
st.write('**Disadvantages**')
st.write(' - Apps all look the same')
st.write(' - Not very customizable')
st.write(' - A little slow. Not good for MLOps, therefore not scalable')
