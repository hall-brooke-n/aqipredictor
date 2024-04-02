# Capstone Project - Air Quality Index Predictor
Brooke Hall

## Project Overview

The area of interest is that with the possible decline in air quality due to global warming, susceptible individuals need to be able to understand which areas are safe to live and which will become higher risk in coming years in the United States.

This model shall predict the safest states for succeptible populations (respiratory succeptibility) to live in the next 5-10 years. This model uses environmental monitoring data to calculate projected Air Quality Index (AQI) with a time series model.


### Problem:
 Increases in pollution, emissions and temperature due to global warming are resulting in increasingly worse air quality. For people with susceptible lungs and environmental sensitivities, the air quality in their local environment is pivotal for living a healthy lifestyle. 


### Impact:
 This will add societal value for individuals who are susceptible to changes in their living environment. It can arm them with better understanding of what to expect in coming years and better prepare their homes and/or know where to move to. Additionally, government or environmental organizations looking to implement environmental policy. Have a better understanding of trends and recommended locations. Possible incentive for groups looking to push environmental policy.


### Description of Data:
 Data includes Air Quality Index (AQI) monitoring data from the United States Environmental Protection Agency. There are two main types of yearly files that have been pulled and joined:
 	
 	1. AQI - See data dictionary Monitor Description File (https://aqs.epa.gov/aqsweb/airdata/FileFormats.html)
 		- Daily calculated AQI by location (City, County, State)
 		- Includes Sentiment of AQI
 		- Includes key parameter - parameter that most affects calculations

 	2. Daily Summary Files - Data Dictionary
 		- Daily monitoring data collection by location (City, County, State)
 		- Means of samples reported/calculated per Method and Parameter
 		- If an event occured (i.e. wildfires), this is recorded

 	3. Site Description File - Data Dictionary
 		- Includes site location information, including latitude and longitude

 These three files were combined into one large table for review. 

 Note - Critical Gas and Particulate Contaminant files are not included in the combined Daily Summary File as these values are used to calculate AQI. They are to be excluded in the model and only referenced by largest impact.

 
## Project Organization

•	Data
	 - Link to the datasets in Google Drive: https://drive.google.com/drive/folders/1Qh8JM_xaESutNF0Y1V1Fn3nYpuVVA1SW?usp=sharing 

•	Notebooks
	- 01_Data_Pull_EDA_AQI_Prediction.ipynb
	- 02_Preliminary_Modeling.ipynb
	- timeseries.yml - kernel for notebooks

•	Models
	- Optimized univariate prophet models (1 per US state)
	
•	Streamlit
	- The start of a streamlit script for data interactivity

•	Credits & References
		
	1   United States Environmental Protection Agency: https://aqs.epa.gov/aqsweb/airdata/download_files.html
	2	Kaggle for Daily AQI: https://www.kaggle.com/datasets/threnjen/40-years-of-air-quality-index-from-the-epa-daily
	3	Data Dictionary: https://aqs.epa.gov/aqsweb/airdata/FileFormats.html



