import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_sentiment_analyser():
    return pipeline("sentiment-analysis")

def main():
    try:
        st.title("Sentiment Analyser")
        st.markdown(''' This app analyses your feelings based on the input text given by the user''')
        input = st.text_area("Enter your input Text" , height=200)
        analyse_button = st.button("Analyse Text")
        if analyse_button:
         if input.strip() :
            sentiment_analyser = load_sentiment_analyser()
            result = sentiment_analyser(input)
            st.write(result)
        
         else:
           st.error("INVALID TEXT")
    
    except Exception as e:
        st.error(e)

if __name__=="__main__":
    main()
