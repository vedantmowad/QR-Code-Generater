import qrcode
import streamlit as st
import datetime
from io import BytesIO
import os

t1, t2 = st.tabs(["QR Code Generator", "History"])

with t1:
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
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        st.image(buffer, caption="Generated QR Code")
        if st.download_button("Download QR Code", 
                            data=buffer.getvalue(),
                            file_name=f"{name}.png",
                            mime="image/png"
                            ):
            st.success("QR Code downloaded successfully!")

with t2:
    st.title("📜History")
    st.write("This section will display the history of generated QR codes.")
    image_folder = "images"
    cols = st.columns(3)
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            for i in range(len(cols)):
                cols[i].image(image_path, caption=f"**{filename}**")
                if i == len(cols) - 1:
                    i = 0
