import streamlit as st
from PIL import Image


# Configure the page
def main():
    st.set_page_config(page_title="SDG Navigator", layout="centered")

    # Title of the app
    st.title("Welcome to SDG Navigator")

    # Creating placeholders for images
    col1, col2, col3 = st.columns([1, 1, 1])
    col4, col5, col6 = st.columns([1, 1, 1])
    col7, col8, col9 = st.columns([1, 1, 1])
    col10, col11, col12 = st.columns([1, 1, 1])
    col13, col14 = st.columns([1, 1])

    # First row of images with links
    with col1:
        if st.button("Image 1"):
            st.experimental_rerun()  # Redirect to another page logic

    with col2:
        if st.button("Image 2"):
            st.experimental_rerun()  # Redirect to another page logic

    with col3:
        if st.button("Image 3"):
            st.experimental_rerun()  # Redirect to another page logic

    # Second row of images with links
    with col4:
        if st.button("Image 4"):
            st.experimental_rerun()  # Redirect to another page logic

    with col5:
        if st.button("Image 5"):
            st.experimental_rerun()  # Redirect to another page logic

    with col6:
        if st.button("Image 6"):
            st.experimental_rerun()  # Redirect to another page logic

    # Third row of images with links
    with col7:
        if st.button("Image 7"):
            st.experimental_rerun()  # Redirect to another page logic

    with col8:
        if st.button("Image 8"):
            st.experimental_rerun()  # Redirect to another page logic

    with col9:
        if st.button("Image 9"):
            st.experimental_rerun()  # Redirect to another page logic

    # Fourth row of images with links
    with col10:
        if st.button("Image 10"):
            st.experimental_rerun()  # Redirect to another page logic

    with col11:
        if st.button("Image 11"):
            st.experimental_rerun()  # Redirect to another page logic

    with col12:
        if st.button("Image 12"):
            st.experimental_rerun()  # Redirect to another page logic

    # Fifth row of images with links
    with col13:
        if st.button("Image 13"):
            st.experimental_rerun()  # Redirect to another page logic

    with col14:
        if st.button("Image 14"):
            st.experimental_rerun()  # Redirect to another page logic

    # Adding three more images
    col15, col16, col17 = st.columns([1, 1, 1])

    with col15:
        if st.button("Image 15"):
            st.experimental_rerun()  # Redirect to another page logic

    with col16:
        if st.button("Image 16"):
            st.experimental_rerun()  # Redirect to another page logic

    with col17:
        if st.button("Image 17"):
            st.experimental_rerun()  # Redirect to another page logic

    # Option for user to start chat
    st.markdown("<div style='text-align: center; margin-top: 20px;'> OR </div>", unsafe_allow_html=True)
    chat_box = st.text_input("Type to start chat")
    if chat_box:
        st.write(f"User input: {chat_box}")


if __name__ == "__main__":
    main()
