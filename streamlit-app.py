import streamlit as st
from PIL import Image
import ktrain
import re

emotion_clf = ktrain.load_predictor('mgsa-ed')

def predict_emotion(data):
    result= emotion_clf.predict([data])
    return result

def load_images(file_name):
    img = Image.open(file_name)
    return st.image(img,width=None)

emotions_emoji_dict = {"anger":"😠","disgust":"🤢", "fear":"😨", "joy":"😀", "guilt":"😔", "sadness":"☹️", "shame":"😳"}

st.cache(persist=True)
def call(text):
    if st.button("Predict"):
        if text:
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)

            for sent in m:
                result = predict_emotion(sent) 

                emotion = result[0]

                emoji = emotions_emoji_dict[emotion]

                st.success('{} : {} {}'.format(sent, emotion, emoji))
        else:
            st.error("Please enter a valid input")

def main():
    """Emotion Detection App
    With Streamlit

    """

    st.title("FGSA- Emotion Detection")
    html_temp = """
    <div style="background-color:white;padding:0px">
    <h2 style="color:black;text-align:center;">See which emotion is in your text: </h2>
    </div>

  """
    st.markdown(html_temp,unsafe_allow_html=True)
    load_images('emotions.jpg')

    text = st.text_input("Please Type Below")
    call(text)

if __name__ == "__main__":
    main()
