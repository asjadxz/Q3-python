import streamlit as st
import re  

# Title for the web app
st.title("Grade Sheet Generator")

# Streamlit widgets to get user input
name = st.text_input("Enter your name: ")
age = st.number_input("Enter your age: ", min_value=1, max_value=150, value=18)
Class = st.text_input("Enter your class: ")
max_marks = st.number_input("Enter Maximum Marks: ", min_value=1.0)
obt_marks = st.number_input("Enter Obtained Marks: ", min_value=0.0, max_value=max_marks)

# Error handling with try-except block
if st.button("Calculate Grade"):
    try:
        # Validate name to ensure it only contains alphabets
        if not re.match("^[A-Za-z ]*$", name):
            raise ValueError("Name must contain only alphabets and spaces.")
        
        # Check if max_marks is greater than zero
        if max_marks <= 0:
            raise ValueError("Maximum marks must be greater than zero.")

        result = (obt_marks / max_marks) * 100
        grade = ''

        # Assigning grades based on percentage
        if result >= 90:
            grade = "A+"
        elif result >= 80 and result < 90:
            grade = "B+"
        elif result >= 70 and result < 80:
            grade = "C+"
        elif result >= 60 and result < 70:
            grade = "D+"
        elif result >= 50 and result < 60:
            grade = "E+"
        else:
            grade = "F"
        
        # Display grade sheet
        st.subheader("***GRADE SHEET***")
        st.write(f"**Name**: {name}")
        st.write(f"**Age**: {age}")
        st.write(f"**Class**: {Class}")
        st.write(f"**Marks Obtained**: {obt_marks}")
        st.write(f"**Out of**: {max_marks}")
        st.write(f"**Percentage**: {result:.2f}%")
        st.write(f"**Grade**: {grade}")
    
    except ValueError as e:
        # Handle invalid input (e.g., non-alphabet name or zero max_marks)
        st.error(f"Error: {e}")
    except Exception as e:
        # Catch any other errors
        st.error(f"An unexpected error occurred: {e}")
