import streamlit as st
import os
import zipfile
import requests

# Function to save uploaded file to the specified directory
def save_uploaded_file(uploaded_file, save_dir):
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.read())
    return file_path

# Function to save uploaded folder (as a zip file) and extract it
def save_and_extract_folder(uploaded_zip, save_dir):
    zip_path = os.path.join(save_dir, uploaded_zip.name)
    with open(zip_path, 'wb') as f:
        f.write(uploaded_zip.read())

    extract_dir = os.path.join(save_dir, uploaded_zip.name[:-4])  # Remove .zip extension
    os.makedirs(extract_dir, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir

# Function to perform an AI-based code review for Python files using an Ollama server
def code_review_ai(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    # Use Ollama server to analyze the code
    server_url = "http://100.114.84.111"
    model_name = "llama3.2:latest"
    
    payload = {
        "model": model_name,
        "prompt": f"You are a helpful assistant skilled in reviewing Python code for best practices, bugs, and improvements. Please review the following Python code and provide feedback on any issues or improvements:\n\n{code}"
    }

    response = requests.post(f"{server_url}/chat", json=payload)
    response_data = response.json()

    if response.status_code == 200 and "response" in response_data:
        return response_data["response"]
    else:
        return "Error: Unable to get a response from the AI server."

# Main Streamlit app
def main():
    st.set_page_config(layout="wide")
    st.title("AI-Powered Python Code Reviewer")

    # Create a directory to save uploaded files
    save_dir = "uploaded_files"
    os.makedirs(save_dir, exist_ok=True)

    # Set up columns with equal width and bordered containers
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown(
            "<div style='border: 2px solid #ddd; padding: 15px; border-radius: 5px; height: 100%;'>",
            unsafe_allow_html=True
        )
        st.header("Upload a Document or a Folder")
        uploaded_file = st.file_uploader("Choose a Python file or zipped folder", type=["py", "zip"])
        if uploaded_file:
            if uploaded_file.name.endswith('.zip'):
                extracted_path = save_and_extract_folder(uploaded_file, save_dir)
                st.success(f"Folder extracted at: {extracted_path}")
            else:
                file_path = save_uploaded_file(uploaded_file, save_dir)
                st.success(f"File saved at: {file_path}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            "<div style='border: 2px solid #ddd; padding: 15px; border-radius: 5px; height: 100%;'>",
            unsafe_allow_html=True
        )
        st.header("Code Review")
        if uploaded_file and uploaded_file.name.endswith('.py'):
            file_path = os.path.join(save_dir, uploaded_file.name)
            review = code_review_ai(file_path)
            st.subheader("AI Code Review")
            st.text_area("Review Details", value=review, height=500)
        st.markdown("</div>", unsafe_allow_html=True)

    # Display uploaded files and directories
    st.header("Uploaded Files and Folders")
    if os.listdir(save_dir):
        for root, dirs, files in os.walk(save_dir):
            level = root.replace(save_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            st.text(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                st.text(f"{subindent}{file}")
    else:
        st.write("No files uploaded yet.")

if __name__ == "__main__":
    main()
