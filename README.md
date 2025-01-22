AI-Powered Python Code Reviewer

This project is a Streamlit-based web application designed to review Python code using an AI model hosted on an Ollama server. The app provides developers with a tool to upload Python files or zipped folders, performs a code review, and offers suggestions for improving code quality and identifying potential issues.

Features

Upload Python Files: Upload individual .py files for review.

Upload Zipped Folders: Upload zipped folders containing multiple Python scripts or repos for batch processing.

AI Code Review: The application uses the the Ollama model of your choice on to provide feedback on best practices, potential bugs, and areas for improvement.

Clean User Interface: Responsive design with separate sections for file uploads and review results.

Wide Layout: Optimized for better visibility with bordered containers for each section.

Requirements

Python Packages

Install the required packages using the following command:

pip install -r requirements.txt

Required Libraries

Streamlit: For building the web application.

Requests: For communication with the Ollama server.

Zipfile: For extracting zipped folders.

OS: For file management.

Setup

1. Clone the Repository

git clone <repository_url>
cd <repository_folder>

2. Configure the Ollama Server

Update the code_review_ai function with the correct server URL and AI model:

Ollama Server URL: http://X.X.X.X

Model: llama3.2:latest

Ensure the Ollama server is up and running at the specified address.

How to Run

Run the Streamlit app:

streamlit run <script_name>.py

Open the app in your browser at:

http://localhost:8501

Use the left panel to upload Python files or zipped folders.

View the AI-powered code review results in the right panel.

Project Structure

project_root/
│
├── main.py       # Main Python script for the app
├── requirements.txt       # Dependencies for the project
├── .gitignore             # Ignore uploaded_files and other unnecessary files
└── README.md              # Documentation for the project

Contributing

Feel free to fork this repository, submit pull requests, or suggest features by opening issues.