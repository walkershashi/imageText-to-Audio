import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image

from text_to_speech import speak_text
from recognize_text import recognize_text


st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Image-to-Audio')


st.subheader("Upload")
uploaded_file = st.file_uploader("Choose an image...", type = "jpg")

if uploaded_file is not None:
    org_image = Image.open(uploaded_file)

    # Convert to Open-CV image
    opencv_image = cv2.cvtColor(np.array(org_image), cv2.COLOR_RGB2BGR)

    if st.button('Get Image'):
        st.image(opencv_image, caption = 'Uploaded_Image', use_column_width = True)

    

if st.button("Get Audio"):
    text = recognize_text(opencv_image)
    speak_text(text)
    #x_test, y_test, nb_classifier = train_model()
    #label = get_label(nb_classifier, x_test)
    #print(classification_report(y_test, label))
    #df = pd.DataFrame(classification_report(y_test, label))

    #st.dataframe(df)

    audio_file = open('./temp.mp3', "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
