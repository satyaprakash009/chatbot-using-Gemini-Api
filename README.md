# Q&A chatbot-using-Gemini-Api
a chatbot using the Gemini API that can remember previous inputs and outputs,  implement a persistent chat session that maintains context across user interactions.

This repository contains a Streamlit application that interacts with the Gemini Pro model from Google Generative AI. The application allows users to ask questions and receive responses from the AI model, maintaining a chat history for the session.

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Configuration](#configuration)


## Demo

### Video Demo
Watch the video demo of the application in action:

![Video Demo]([QA chatbot demo.webm](https://github.com/satyaprakash009/chatbot-using-Gemini-Api/blob/main/QA%20chatbot%20demo.webm))

### Image Demo
Here are some screenshots of the application:

![Demo Image]([QA_chatbot.png](https://github.com/satyaprakash009/chatbot-using-Gemini-Api/blob/main/QA%20chatbot.PNG))  <!-- Add a screenshot of your application -->

## Features

- Interactive Q&A with the Gemini Pro model.
- Persistent chat history for the session.
- Easy-to-use Streamlit interface.

## Installation

To get started with the application, follow these steps:

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/username/repo.git
    cd repo
    ```

2. **Create and Activate a Virtual Environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set Up Environment Variables**:
   
   Create a `.env` file in the root directory of the project and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

2. **Run the Application**:

    ```sh
    streamlit run mem.py
    ```

3. **Interact with the Chatbot**:
   - Open the URL provided by Streamlit in your browser.
   - Enter your questions in the input box and press the "Ask the question" button.
   - View the responses and chat history in the Streamlit interface.

## Requirements

The application requires the following Python packages:

- `streamlit`
- `python-dotenv`
- `google-generativeai`

These dependencies are listed in the `requirements.txt` file and can be installed using `pip install -r requirements.txt`.

## Configuration

The application uses environment variables to configure the Google API key. Make sure to create a `.env` file with the following content:

```env
GOOGLE_API_KEY=your_google_api_key_here
