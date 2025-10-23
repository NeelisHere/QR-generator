import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔳", layout="centered")

st.title("🔳 QR Code Generator")
st.write("Enter a URL or text below to generate a downloadable QR code.")

# User Input
user_input = st.text_area("Enter URL or Text")

if st.button("Generate QR Code"):
    if user_input.strip() == "":
        st.warning("Please enter some text or a URL.")
    else:
        # Generate QR with smaller size
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=6,  # smaller box size
            border=2,    # smaller border
        )
        qr.add_data(user_input)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to bytes
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Center and display smaller image
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(byte_im, caption="Generated QR Code")

        # Download Button
        st.download_button(
            label="📥 Download QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
