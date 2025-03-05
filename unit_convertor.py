import streamlit as st

# Making title
st.title("Unit Converter")

# Creating main dropdown list
units = ["Length / Distance", "Mass / Weight", "Volume / Capacity", "Temperature"]

# Creating semi dropdown lists for specific conversions
units_l = ["Meters (m) ↔ Kilometers (km)", "Miles (mi) ↔ Kilometers (km)", "Inches (in) ↔ Centimeters (cm)"]
units_m = ["Kilograms (kg) ↔ Grams (g)", "Pounds (lbs) ↔ Kilograms (kg)", "Ounces (oz) ↔ Grams (g)"]
units_v = ["Liters (L) ↔ Milliliters (mL)", "Cups (cup) ↔ Milliliters (mL)", "Cubic meters (m³) ↔ Liters (L)"]
units_t = ["Celsius (°C) ↔ Fahrenheit (°F)", "Celsius (°C) ↔ Kelvin (K)", "Fahrenheit (°F) ↔ Kelvin (K)"]

# Variable for catching selected unit type
selected_unit = st.selectbox("Choose a unit type to convert:", units)

# Variable for catching second dropdown selection
selected_unit2 = ''

# Adding conditions for each unit type
if selected_unit == "Length / Distance":
    selected_unit2 = st.selectbox("Choose the conversion:", units_l)
    if selected_unit2 == "Meters (m) ↔ Kilometers (km)":
        num1 = st.number_input("Enter meters:", min_value=1)
        num2 = num1 / 1000  # Conversion from meters to kilometers
        st.write("Kilometers = Meters / 1000")
        st.write(f"{num1} meters = {num2} kilometers")
    elif selected_unit2 == "Miles (mi) ↔ Kilometers (km)":
        num1 = st.number_input("Enter miles:", min_value=1)
        num2 = num1 * 1.60934  # Conversion from miles to kilometers
        st.write("Kilometers = Miles * 1.60934")
        st.write(f"{num1} miles = {num2} kilometers")
    elif selected_unit2 == "Inches (in) ↔ Centimeters (cm)":
        num1 = st.number_input("Enter inches:", min_value=1)
        num2 = num1 * 2.54  # Conversion from inches to centimeters
        st.write("Centimeters = Inches * 2.54")
        st.write(f"{num1} inches = {num2} centimeters")

elif selected_unit == "Mass / Weight":
    selected_unit2 = st.selectbox("Choose the conversion:", units_m)
    if selected_unit2 == "Kilograms (kg) ↔ Grams (g)":
        num1 = st.number_input("Enter kilograms:", min_value=1)
        num2 = num1 * 1000  # Conversion from kilograms to grams
        st.write("Grams = Kilograms * 1000")
        st.write(f"{num1} kilograms = {num2} grams")
    elif selected_unit2 == "Pounds (lbs) ↔ Kilograms (kg)":
        num1 = st.number_input("Enter pounds:", min_value=1)
        num2 = num1 * 0.453592  # Conversion from pounds to kilograms
        st.write("Kilograms = Pounds * 0.453592")
        st.write(f"{num1} pounds = {num2} kilograms")
    elif selected_unit2 == "Ounces (oz) ↔ Grams (g)":
        num1 = st.number_input("Enter ounces:", min_value=1)
        num2 = num1 * 28.3495  # Conversion from ounces to grams
        st.write("Grams = Ounces * 28.3495")
        st.write(f"{num1} ounces = {num2} grams")

elif selected_unit == "Volume / Capacity":
    selected_unit2 = st.selectbox("Choose the conversion:", units_v)
    if selected_unit2 == "Liters (L) ↔ Milliliters (mL)":
        num1 = st.number_input("Enter liters:", min_value=1)
        num2 = num1 * 1000  # Conversion from liters to milliliters
        st.write("Milliliters = Liters * 1000")
        st.write(f"{num1} liters = {num2} milliliters")
    elif selected_unit2 == "Cups (cup) ↔ Milliliters (mL)":
        num1 = st.number_input("Enter cups:", min_value=1)
        num2 = num1 * 236.588  # Conversion from cups to milliliters
        st.write("Milliliters = Cups * 236.588")
        st.write(f"{num1} cups = {num2} milliliters")
    elif selected_unit2 == "Cubic meters (m³) ↔ Liters (L)":
        num1 = st.number_input("Enter cubic meters:", min_value=1)
        num2 = num1 * 1000  # Conversion from cubic meters to liters
        st.write("Liters = Cubic meters * 1000")
        st.write(f"{num1} cubic meters = {num2} liters")

elif selected_unit == "Temperature":
    selected_unit2 = st.selectbox("Choose the conversion:", units_t)
    if selected_unit2 == "Celsius (°C) ↔ Fahrenheit (°F)":
        num1 = st.number_input("Enter Celsius:", min_value=-273.15)  # Min value is absolute zero
        num2 = (num1 * 9/5) + 32  # Conversion from Celsius to Fahrenheit
        st.write("Fahrenheit = (Celsius * 9/5) + 32")
        st.write(f"{num1}°C = {num2}°F")
    elif selected_unit2 == "Celsius (°C) ↔ Kelvin (K)":
        num1 = st.number_input("Enter Celsius:", min_value=-273.15)  # Min value is absolute zero
        num2 = num1 + 273.15  # Conversion from Celsius to Kelvin
        st.write("Kelvin = Celsius + 273.15")
        st.write(f"{num1}°C = {num2}K")
    elif selected_unit2 == "Fahrenheit (°F) ↔ Kelvin (K)":
        num1 = st.number_input("Enter Fahrenheit:", min_value=-459.67)  # Min value is absolute zero in Fahrenheit
        num2 = (num1 - 32) * 5/9 + 273.15  # Conversion from Fahrenheit to Kelvin
        st.write("Kelvin = (Fahrenheit - 32) * 5/9 + 273.15")
        st.write(f"{num1}°F = {num2}K")
