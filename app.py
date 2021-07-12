import streamlit as st

# url video: https://www.youtube.com/watch?v=_9WiB2PDO7k&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU

# Text/Title
st.title("Streamlit tutorial")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorfull Text
st.success("Succesful")

st.info("Information")

st.warning("This is a warning")

st.error("This is an error Danger")

#st.exception("NameError('name "three" not define')")
st.exception("NameError('name three not define')")


# Get help info about Python
st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")
st.write(range(10))

# Images
from PIL import Image

img = Image.open("1080x1080.webp")
st.image(img, width=300, caption="Nienke and Nacho")

# Video
# video_file = open("example.mp4", "rb").read()
# st.video(video_file)

# Audio
# audio_file = open("example.mp3", "rb").read()
# st.audio(audio_file, format="audio/mp3")

# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
else:
    st.warning("Your are inactive")

# SelectBox
occupation = st.selectbox(
    "Your ocuppation", ["Programmer", "DataScientist", "Doctor", "Businessman"]
)
st.write("You selected this option: ", occupation)

# Multiselect
location = st.multiselect("Where do you work?", ["London", "USA", "Spain", "Portugal"])
st.write("You selected", len(location), "locations")

# Slider
level = st.slider("What is your level",1,5)

# Buttons
st.button("Simple button")

if st.button("About"):
    st.write("Streamlit is cool")

# Text Input
firstname = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)


# Text Area
message = st.text_area("Enter your message", "Type here...")
if st.button("Message"):
    result = message.title()
    st.success(result)


# Date Input
import datetime
today = st.date_input("Today is ", datetime.datetime.now())

# Time
the_time = st.time_input("The time is", datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({"name":"Nacho", "gender":"male"})

# Display Raw code
st.text("Display Raw code")
st.code("import numpy as np")

# Display Raw code
with st.echo():
    # This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()


# Progress bar
import time
my_progress_bar = st.progress(0)
for p in range(50):
    my_progress_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

# Ballons
st.balloons()


# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is a streamlit tutorial")


# Funtions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())


# Plot
#st.pyplot()


# Dataframe
st.dataframe(df)

# Table
st.table(df)