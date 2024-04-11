### KICKOFF - CODING AN APP IN STREAMLIT

#conda install -c conda-forge streamlit

### import libraries
import pandas as pd
import streamlit as st
import joblib
import plotly.express as px


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



#######################################################################################################################################
### Create a title

st.title("Air Quality Index Predictor")
#st.markdown("<h1 style='text-align: center; color: blue;'>Air Quality Index Predictor</h1>", unsafe_allow_html=True)
st.write('The included models predict aqi depending on environmental monitoring factors.')

# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
# st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
### DATA LOADING


### A. define function to load data
@st.cache_data # <- add decorators after tried running the load multiple times
def load_data(path, num_rows):

    df = pd.read_csv(path, index_col = 0, parse_dates = ['Month_Date'], nrows=num_rows)

    # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates
    #df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})  
    df['Year']  = df['Month_Date'].dt.year 
     
    return df

### B. Load first 50K rows
df = load_data("/Users/brookehall/Documents/models/best_prophet/final_forecast_dataset.csv", 50000)

# Load Sentiment
#path2 = '/Users/brookehall/Desktop/Brainstation/Deliverables/CapstoneFolder/capstoneWorking/data/cleanData/'
#f_score = pd.read_csv(path2 + 'dimAQUISentiment.csv', index_col = 0)

#path = '/Users/brookehall/Documents/models/best_prophet/'
#combined_data = pd.read_csv(path+'aqi_multivar.csv')
#st.dataframe(combined_data)


#st.dataframe(df_score)


#######################################################################################################################################
### STATION MAP

# Streamlit Cholorpleth Map title
st.subheader('Interactive AQI Prediction Map of the United States')  

# Add a brief description or instructions
st.write('This choropleth map visualizes the average AQI by state over time.')    

# To make trends easier to see, group by year
aqi_state_year = df.groupby(['State Name', 'State Abbreviation', 'Year'])['aqi'].agg(['mean', 'max', 'min']).reset_index()

# Create the yearly choropleth plot
fig = px.choropleth(df, 
                    locations='State Abbreviation', 
                    locationmode='USA-states',  # Assuming USA states
                    color='aqi', 
                    color_continuous_scale=px.colors.sequential.Blues, 
                    animation_frame='Month_Date',  # Assuming 'Month_Date' column contains the dates
                    title='Air Quality Index by State',
                    scope='usa',
                    labels={'aqi': 'Average AQI', 'Month_Date': 'Date'}, # rename custom data for better readability
                    hover_name='State Name',  # Name shown in the hover label
                    custom_data=['aqi'],
                    range_color = [0, 80])  # Additional data to include in the hover label

fig.update_layout(
    margin={'r':0,'t':30,'l':0,'b':0},
    coloraxis_colorbar={'title':'AQI'}
)
    

# Update hover label format
#fig.update_traces(hovertemplate='<b>%{hovertext}</b><br><br>' +
 #                                'Average AQI: %{customdata[0]}<br>')

# Display the plot in the Streamlit app
st.plotly_chart(fig)

# Show the plot
#fig.show()

#######################################################################################################################################
### DATA ANALYSIS & VISUALIZATION

### B. Add filter on side bar after initial bar chart constructed

st.subheader('State Specific Analysis') 

st.sidebar.subheader("States")
states_list = list(df['State Name'].unique())
state_selection = st.selectbox('Select', states_list)
#multi_state_selection = st.multiselect('multiselect', states_list)

# get mask
mask_selection = df['State Name'] == state_selection
#mask_selection_multi = df['State Name'].apply(lambda x: any(name in x for name in multi_state_selection)) == False

#st.slider('Pick a number', 0, 100)

# Load your data (replace this with your actual data loading code)
# Assuming your DataFrame has columns 'x_values', 'y_values', 'y_error'
# You should replace these with your actual column names

# First create a function that can be called based on different category sentiment levels

st.subheader("Monthly AQI")

# Create the interactive line plot with error bars using Plotly Express
fig = px.line(
    df[mask_selection], 
    x='Month_Date', 
    y='aqi'
    )

# Add horizontal color blocks based on different ranges
fig.add_hrect(y0 = 0, y1 = 50, fillcolor="green", opacity=0.25, layer="below", line_width=0)
fig.add_hrect(y0 = 51, y1 = 100, fillcolor="yellow", opacity=0.25, layer="below", line_width=0)
fig.add_hrect(y0 = 101, y1 = 150, fillcolor="orange", opacity=0.25, layer="below", line_width=0)
fig.add_hrect(y0 = 151, y1 = 200, fillcolor="red", opacity=0.25, layer="above", line_width=0)

# Customize the plot layout
fig.update_layout(
    title='Interactive Line Plot with Error Bars',
    xaxis_title='AQI Value',
    yaxis_title='Year'#,
    #legend='State Name'
)


# Display the plot in the Streamlit app
st.plotly_chart(fig)

#if states_list:
#    df = df[df['Start Station ID'] == df['End Station ID']]


### A. Add a bar chart of usage per hour

#counts = df["Month_Date"].value_counts()
#st.bar_chart(counts)


### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
#### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
#### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
#### Automating processes and handling real-time data


#######################################################################################################################################
### MODEL INFERENCE

st.subheader("Raw Datafile with Predictions")

### C. Display the dataframe in the app
st.dataframe(df)

# A. Load the model using joblib
#model = joblib.load('sentiment_pipeline.pkl')

# B. Set up input field
#text = st.text_input('Enter your review text below', 'Best. Restaurant. Ever.')

# C. Use the model to predict sentiment & write result
#prediction = model.predict({text})

#if prediction == 1:
#    st.write('We predict that this is a positive review!')
#else:
#    st.write('We predict that this is a negative review!')


