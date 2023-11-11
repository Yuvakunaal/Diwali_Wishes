import streamlit as st
import streamlit.components.v1 as com
import json
from streamlit_lottie  import st_lottie

with open("Animation - 1699723958293.json") as source :
    animation1 = json.load(source)
st_lottie(animation1,speed=1.5,height=0,width=375)


st.markdown('''
<!DOCTYPE html>
<html>
<head>
<h6 class=head>Wish you all a very</h6>
<h1 class="heading1">🧨 Happy Diwali 🧨</h1>
<br>
<h4 class="heading2">-- Kunaal</h4>
<style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        .background {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
        }
        .st-emotion-cache-6q9sum
        {
            visibility : hidden;
        }
        .st-emotion-cache-cio0dv
        {
            visibility : hidden;
        }
        .st-emotion-cache-1wbqy5l
        {
            visibility : hidden;
        }
        .heading1
        {
            text-align : center;
        }
        .heading2
        {
            text-align : right;
        }
        .head
        {
            text-align : center;
        }
</style>
</head>
</html>

''',unsafe_allow_html=True)






