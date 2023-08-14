import pandas as pd
import numpy as np
import streamlit as st
import pickle
import sklearn

df = pd.read_csv("cleaned_laptop_data.csv")
pipe = pickle.load(open("pipe.pkl", "rb"))

# st.title("Laptop Price Predictor")
st.markdown("<h1 style='text-align: center;'>Laptop Price Predictor</h1>", unsafe_allow_html=True)

row1c1, row1c2, row1c3 = st.columns(3)
with row1c1:
    company = st.selectbox("Company Name", ["None"] + sorted(list(df["Company"].unique())))
with row1c2:
    Type = st.selectbox("Type", ["None"] + sorted(list(df["TypeName"].unique())))
with row1c3:
    size = st.selectbox("Screen Size", ["None"] + sorted(list(df["Inches"].unique())))

row2c1, row2c2, row2c3 = st.columns(3)
with row2c1:
    ram = st.selectbox("Ram(in GB)", ["None"] + sorted(list(df["Ram"].unique())))
with row2c2:
    wt = st.selectbox("Weight", ["None"] + sorted(list(df["Weight"].unique())))
with row2c3:
    ips = st.selectbox("IPS Panel", ["None"] + sorted(list(df["IPS Panel"].unique())))

row4c1, row4c2 = st.columns(2)
with row4c1:
    processor = st.selectbox("Processor", ["None"] + sorted(list(df["Processor"].unique())))
with row4c2:
    speed = st.selectbox("Processor Speed", ["None"] + sorted(list(df["Speed"].unique())))

row3c1, row3c2, row3c3 = st.columns(3)
with row3c1:
    display = st.selectbox("Display Type", ["None"] + sorted(list(df["Display"].unique())))
with row3c2:
    touch = st.selectbox("Touch Screen", ["None"] + sorted(list(df["TouchScreen"].unique())))
with row3c3:
    res = st.selectbox("Resolution", ["None"] + sorted(list(df["Resolution"].unique())))

row5c1, row5c2, row5c3, row5c4 = st.columns(4)
with row5c1:
    ssd = st.selectbox("SSD(in GB)", ["None"] + sorted(list(df["SSD"].unique())))
with row5c2:
    hdd = st.selectbox("HDD(in GB)", ["None"] + sorted(list(df["HDD"].unique())))
with row5c3:
    hybrid = st.selectbox("Hybrid(in GB)", ["None"] + sorted(list(df["Hybrid"].unique())))
with row5c4:
    flash = st.selectbox("Flash Storage(in GB)", ["None"] + sorted(list(df["Flash_Storage"].unique())))

row6c1, row6c2 = st.columns(2)
with row6c1:
    card = st.selectbox("Graphics Card", ["None"] + sorted(list(df["Graphics_Card"].unique())))
with row6c2:
    os = st.selectbox("Operating System", ["None"] + sorted(list(df["OS"].unique())))

if st.button("Predict Price", use_container_width=True):
    try:
        fres = int(res.split("x")[0])
        sres = int(res.split("x")[1])

        pred = pipe.predict(pd.DataFrame([[company, Type, size, ram, wt, ips, display, touch, fres, sres, processor, speed,
                                           ssd, hdd, hybrid, flash, card, os]],
                                         columns=["Company", "TypeName", "Inches", "Ram", "Weight", "IPS Panel", "Display",
                                                  "TouchScreen", "First_Res", "Second_Res", "Processor", "Speed", "SSD",
                                                  "HDD",
                                                  "Hybrid", "Flash_Storage", "Graphics_Card", "OS"]))

        label = "Predicted Price : ₹ " + "{:,}".format(int(np.round(np.exp(pred[0]), 0)))
        centered_bold_label = f"<h3 style='text-align: center;'><b>{label}</b></h3>"
        st.write(centered_bold_label, unsafe_allow_html=True)
        # st.write("Prediction : ₹", predict_price())
    except:
        st.error("Select From Every Option")
