import streamlit as st
import pretty_errors
from docarray import Document
from config import SERVER, NUM_IMAGES

prompt = st.text_input("What would you like to generate an image of?")

generate_button = st.button("Generate!")

if generate_button:
    doc = Document(text=prompt)
    results = doc.post(SERVER, parameters={"num_images": NUM_IMAGES})

    # for match in results.matches:
        # print(match.content)
        # st.image(match.uri)

    st.image(results.matches[0].uri)
