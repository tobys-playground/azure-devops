import streamlit as st
import ktrain
import re

emotion_clf = ktrain.load_predictor('./models/outputs')

def predict_emotion(data):
    result= emotion_clf.predict([data])
    return result

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

st.cache(persist=True)
def call(text):
    if st.button("Predict"):
        if text:
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

            for sent in m:
                result = predict_emotion(sent) 

                emotion = result[0]

                st.success('{} : {}'.format(sent, emotion))

        else:
            st.error("Please enter a valid input")

def main():
    """Joy Detector App
    With Streamlit
    """

    st.title("Joy Detector")
    html_temp = """
    <div style="background-color:white;padding:0px">
    <h2 style="color:black;text-align:center;">See if your text contains the emotion of joy or is neutral!</h2>
    </div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)

    text = st.text_input("Please Type Below")
    call(text)
    
if __name__ == "__main__":
    main()