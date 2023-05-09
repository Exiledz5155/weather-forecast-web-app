import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5
                 , help="Select the number of forecasted days") # Creating a slider
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature or sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # For dictionary in data assign/replace with only the temperature
            temperatures = [(dict["main"]["temp"] / 10) * (9/5) + 32 for dict in filtered_data]
            # Grabbing the dates
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Creating a line graph
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Dictionary matching filtered data with png names
            images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            # For dictionary in data assign/replace with only the sky conditions
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # dictionary containing a dictionary containing a list containing a dictionary\

            # For conditions in our data, we want to find the paths to the png files
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist.")