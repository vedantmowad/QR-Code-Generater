import qrcode
import streamlit as st
import datetime

st.title("🔳QR Code Generator")
st.write('''This application generates QR codes based on the input 
            data provided by the user. You can enter any text or URL, 
            and it will create a QR code image that you can download.''')
st.write(f"**Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**")
st.subheader("")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = st.text_input("Enter the data to encode in the QR code:")
name = st.text_input("Enter the name for the QR code image file:")

if st.button("Generate QR Code"):
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"images/{name}.png")
    st.image(f"images/{name}.png", caption="Generated QR Code")