# Global Climate Change Data Analysis Dashboard

This is an interactive web dashboard built using **Streamlit**, **Pandas**, **Matplotlib**, and **Plotly** to analyze and visualize global climate change data from 1975 to 2025 across multiple countries.

---

## Features

- **Multi-language support:** English, Hindi, Spanish, and French interface options.
- **Country and year selectors:** Filter data by country and year.
- **CO₂ Emissions Trend:** Line chart showing CO₂ emissions over time for the selected country.
- **Temperature Anomaly Trend:** Line chart showing temperature anomalies over time for the selected country.
- **Global Sea Level Rise:** Line chart showing average global sea level rise over time.
- **Top CO₂ Emitters:** Interactive bar chart showing top CO₂ emitting countries for the selected year, with hover/touch tooltips.

---

## Installation

1. Clone the repository or download the code files.

2. Install required packages (preferably in a virtual environment):

```bash
pip install streamlit pandas matplotlib plotly
```

# To run the project on terminal
Run your project with this command:-
```
streamlit run app.py
```
# How to use?:-
Select your preferred language from the dropdown.<br>
Choose a country to view CO₂ emissions and temperature anomaly trends.<br>
Choose a year to view the top CO₂ emitters for that year.<br>
Hover or tap on bars in the interactive chart to see detailed values.<br>

# Dataset:-
The dataset global_climate_data_1975_2025.csv contains:

Year: Year of the record (1975–2025)<br>
Country: Country name<br>
CO2_Emissions_Mt: CO₂ emissions in million tonnes<br>
Temp_Anomaly_C: Temperature anomaly in °C<br>
Sea_Level_Rise_mm: Sea level rise in millimeters (global average)

# Customization
Modify the language dictionary in the code to add or change translations.<br>
Change color schemes by updating Plotly color sequences.<br>
Switch between vertical and horizontal bar charts by toggling the orientation parameter in the Plotly bar chart section.

# Dependencies:- 
Python 3.7+<br>
Streamlit<br>
Pandas<br>
Matplotlib<br>
Plotly

# License:-
This project is open source and free to use under the MIT License.
