# import modules

import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Hashtag Generator", page_icon=":hash:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load assets
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_19j4uqeq.json")

# Header
st.title(":hash: Hashtag Generator for Instagram & Facebook :hash:")
st.subheader("Use this tool to generate hashtags for your social media posts!")

# Introduction and instructions on how to use the generator
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("This hashtag generator has been made specifically for Earth's Atelier.")
        st.write("The intended use for this web app is to generate hashtags for social media posts.")
    with right_column:
        st_lottie(lottie_coding, height=300, key="phone")

st.write("---")

def get_hashtags(input_str):
    
    # get hashtag data and load it into raw_data
    url = "https://hashtagy-generate-hashtags.p.rapidapi.com/v1/comprehensive/tags"

    querystring = {"keyword": input_str}

    headers = {
        "X-RapidAPI-Key": "3f3a735fd4msh3d2a78cf4088122p1491ddjsn194cfd4ef345",
        "X-RapidAPI-Host": "hashtagy-generate-hashtags.p.rapidapi.com"
    }

    response = requests.get(url, headers = headers, params = querystring)
    
    raw_data = json.loads(response.text)
    
    # clean data
    # remove unnecessary values from output
    remove_values = ['status', 'status_message', '@meta']
    
    for i in remove_values:
        raw_data.pop(i)
        
    hashtag_list = raw_data['data']['best_30_hashtags']['hashtags']

    clean_hashtags = [i.split(',')[0] for i in hashtag_list]

    top_hashtags = []

    # add hashtag symbols
    for i in clean_hashtags:
        top_hashtags.append('#' + i)        
    
    return top_hashtags
    
# Define the Streamlit app
def main():
    st.title("Hashtag Generator")
    input_str = st.text_input("Enter some text to generate hashtags for:")
    if input_str:
        if st.button("Generate Hashtags"):
            hashtags = get_hashtags(input_str)
            if hashtags:
                st.write("Here are your hashtags:")
                st.write(hashtags)
            else:
                st.warning("No hashtags found.")
    st.write("Made by Julia")

if __name__ == "__main__":
    main()
