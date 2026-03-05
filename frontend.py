import streamlit as st
import requests

st.title("ChandraGPT 🤖 with File Reading")
st.write("Ask questions or upload a file first!")

# File uploader
uploaded_file = st.file_uploader("Upload PDF/CSV/Excel", type=["pdf","csv","xls","xlsx"])

if uploaded_file:
    response = requests.post("http://127.0.0.1:8000/upload", files={"file": uploaded_file})
    st.success(response.json()["message"])
    st.write(f"Chunks processed: {response.json().get('chunks')}")

# Ask question
question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )
            data = response.json()
            if "answer" in data:
                st.success("Answer:")
                st.write(data["answer"])
            else:
                st.error("Error:")
                st.write(data)
        except Exception as e:
            st.error(f"Connection error: {e}")