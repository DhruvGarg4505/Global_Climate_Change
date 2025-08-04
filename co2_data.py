# -------------------- Global climate change ------------------------

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Global Climate Change Data Analysis")
st.set_page_config(page_title="Global Climate Data",
                   layout="wide")

# ------------------- To load file --------------------------------
url = "global_climate_data_1975_2025.csv"

df = pd.read_csv(url)

translations = {
    "English": {
        "title": "Global Climate Change Dashboard",
        "select_country": "Select Country",
        "select_year": "Select Year",
        "co2_trend": "CO₂ Emissions Over Time for",
        "temp_trend": "Temperature Anomaly Over Time for",
        "sea_level": "Global Average Sea Level Rise",
        "top_emitters": "Top CO₂ Emitters in",
    },
    "Hindi": {
        "title": "वैश्विक जलवायु परिवर्तन डैशबोर्ड",
        "select_country": "देश चुनें",
        "select_year": "वर्ष चुनें",
        "co2_trend": "CO₂ उत्सर्जन समय प्रवृत्ति:",
        "temp_trend": "तापमान विचलन समय प्रवृत्ति:",
        "sea_level": "वैश्विक औसत समुद्र स्तर वृद्धि",
        "top_emitters": "शीर्ष CO₂ उत्सर्जक (वर्ष:",
    },
    "Spanish": {
        "title": "Panel de Cambio Climático Global",
        "select_country": "Seleccionar país",
        "select_year": "Seleccionar año",
        "co2_trend": "Emisiones de CO₂ a lo largo del tiempo para",
        "temp_trend": "Anomalía de temperatura a lo largo del tiempo para",
        "sea_level": "Aumento promedio global del nivel del mar",
        "top_emitters": "Principales emisores de CO₂ en",
    },
    "French": {
        "title": "Tableau de Bord du Changement Climatique Mondial",
        "select_country": "Sélectionner un pays",
        "select_year": "Sélectionner une année",
        "co2_trend": "Émissions de CO₂ au fil du temps pour",
        "temp_trend": "Anomalie de température au fil du temps pour",
        "sea_level": "Élévation moyenne du niveau de la mer",
        "top_emitters": "Principaux émetteurs de CO₂ en",
    }
}

# Language selector -----------------
language = st.selectbox("Choose Language", list(translations.keys()))
t = translations[language]

# Use translated labels ------------------
st.title(t["title"])

# --------- Selectors ----------------------
select_country = st.selectbox("Select Country", df["Country"].unique())
select_year = st.selectbox("Select Year", sorted(df["Year"].unique()))

country_data = df[df["Country"] == select_country]


# Emission Trend -------------------
st.subheader(f"{t['co2_trend']} {select_country}")
st.line_chart(country_data.set_index("Year")["CO2_Emissions_Mt"])

# Temperature Trend -------------------
st.subheader(f"{t['temp_trend']} {select_country}")
st.line_chart(country_data.set_index("Year")["Temp_Anomaly_C"])

# Sea Level Trend ----------------------
st.subheader(t["sea_level"])
avg_sea = df.groupby("Year")["Sea_Level_Rise_mm"].mean()
st.line_chart(avg_sea)

# Top emitters ---------------------------
st.subheader(f"{t['top_emitters']} {select_year}")

# Filter and sort data --------------------
top_emitters = df[df["Year"] == select_year].sort_values(
    by="CO2_Emissions_Mt", ascending=False)

# Create Plotly bar chart -------------------------
fig = px.bar(
    top_emitters,
    x="Country",
    y="CO2_Emissions_Mt",
    # orientation = "h",            # To make horizontal bar graph
    color="Country",
    hover_data={"CO2_Emissions_Mt": True, "Country": True},
    color_discrete_sequence=px.colors.qualitative.Bold
)

fig.update_layout(
    xaxis_title="Country",
    yaxis_title="CO₂ Emissions (Mt)",
    showlegend=False,

    # To change y-axis intervals -----------------
    yaxis=dict(
        tick0=0,
        dtick=200,
    ),
    hoverlabel=dict(bgcolor="black", font_size=12, font_family="Arial")
)

# Show interactive chart -------------------------
st.plotly_chart(fig, use_container_width=True)