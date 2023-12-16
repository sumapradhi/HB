import streamlit as st

github_link = "https://github.com/sumapradhi/HB"
st.markdown(f"Check out the code on [GitHub]({github_link})", unsafe_allow_html=True)

# Centered title with custom styling

st.markdown("<h1 style='text-align: center; color: blue ;'>Happy Birthday VARSHA</h1>", unsafe_allow_html=True)

# Image and caption centered with custom styling
image_path = "Varsha.jpg"

st.balloons()

st.image(image_path, use_column_width=False)

caption_style = "font-size: 24px; color: #ff6347; text-align: center;"  # Adjust the font size and color

# Display the caption with custom styles
st.markdown(f"<p style='{caption_style}'>Wishing you many more happy returns of the day. May you be blessed with all good wishes in life.</p>", unsafe_allow_html=True)
