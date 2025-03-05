import re
import streamlit as st 
st.title("Password Strength Meter!")
def password_strength_meter (password):
    score = 0
    #checking length
    if len(password)>=8:
        score +=1
    else:
        st.error("☢ Password should be atleast 8 Characters long! ❌")

    #check for cases
    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score += 1
    else:
        st.error("☢ Password should contain Upper and lower case characters! ❌")

    #check for digits
    if re.search(r'\d',password):
        score +=1
    else:
        st.error("☢ Password should contain atleast one digit [0-9]! ❌")

    #check for special Characters
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/? ]', password):
        score += 1 
    else:
        st.error("☢ Password should contain at least one special character or space! ❌")

    score +=1

    #giving scoring remarks
    if(score <=2):
        strength = "weak"
        st.error(f"Your strength score is {score}")
        st.error(f"Which means your password is {strength}! Please use the mentioned advices to create a strong and secure password!")
    elif(score >2 and score <=4 ):
        strength="Intermediate"
        st.warning(f"Your strength score is {score}")
        st.warning(f"Which means your password is {strength}! Try to make a stronger password for better security!")
    elif(score > 4):
        strength = "Strong"
        st.success(f"Your strength score is {score}")
        st.success(f"Which means your password is {strength}! Great! You have created a strong password")


#list of common passwords
common_passwords = ["password123", "12345678", "123456789", "Password123", "abcdefgh", "password1", "abcd1234", "football", "iloveyou"]

# Ask the user for input 
user_input = st.text_input("Enter your password:")

# Check if the entered password is in the list of common passwords
if user_input:  # Check if the user_input is not empty
    for common_password in common_passwords:
        if user_input == common_password:
            st.error("Come on! Use a creative password!")
            break  # Stop checking after the first match
    else:
     password_strength_meter(user_input)  







    

