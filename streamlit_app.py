import io

import streamlit as st
from PIL import Image

upload = st.file_uploader('Please upload a png file', type='png', accept_multiple_files=False)

if upload is not None:
    image = Image.open(upload)
    st.image(image, caption='Uploaded image')

    angle = st.slider(
        'Rotate image by degrees',
        min_value=-360,
        max_value=360,
        value=0,
        step=45,
    )
    rotated_image = image.rotate(angle, expand=True)

    st.image(rotated_image, caption=f'Rotated image ({angle}°)')

    buffer = io.BytesIO()
    rotated_image.save(buffer, format='PNG')
    buffer.seek(0)

    st.download_button(
        'Download rotated image',
        data=buffer,
        file_name='rotated.png',
        mime='image/png',
    )




audio_file = st.file_uploader('upload an audio file to play', type=['mp3', 'wav'], accept_multiple_files=False)
if audio_file is not None:
    st.audio(audio_file)