# <div align="center"> 🤖 Jarvis AI with OpenAI </div>

<div align="center">
  <img src="https://github.com/ArpitKadam/JARVIS-AI-with-OpenAI/blob/main/images.jpeg" width="450" align="center"/>
</div>

<br>

## ✨ Overview

This project implements a virtual assistant named **Jarvis AI**, powered by OpenAI's cutting-edge API. Jarvis is capable of voice interaction, intelligent response generation, and task automation. It can open websites, play music, provide the current time, and engage in dynamic conversations.

---

## 🚀 Key Features

*   🗣️ **Voice Recognition:** Interact with Jarvis AI using your natural voice.
*   💬 **Chat & Response:** Generates intelligent, context-aware responses using OpenAI's API.
*   ⚙️ **Task Automation:** Opens websites, launches applications, and plays music on command.
*   🧠 **Dynamic Conversations:** Remembers context and maintains the flow of conversation.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

1.  🐍 **Python 3.10+:** Jarvis requires Python 3.10 or later.
2.  📦 **Dependencies:** All necessary packages are listed in `requirements.txt`.
3.  🔑 **OpenAI Account & API Key:** You'll need an OpenAI account and a generated API key.

---

## ⚙️ Setup Instructions

Follow these steps to get Jarvis AI up and running:

### 1. 🔑 Obtain Your OpenAI API Key

1.  Visit the [OpenAI Platform](https://platform.openai.com/).
2.  Sign up or log in to your account.
3.  Navigate to **API Keys** in your account settings.
4.  Generate a new API key and store it securely.

### 2. ⬇️ Set Up Your Environment

1.  Clone the repository:
    ```bash
    git clone https://github.com/ArpitKadam/JARVIS-AI-with-OpenAI.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd JARVIS-AI-with-OpenAI-main
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 3. ⚙️ Configure API Key

*   **Option A (Using `config.py`):**
    *   Open `config.py` and set the `apikey` variable with your API key:
    ```python
    import os
    apikey = "your-api-key"  # Replace with your actual API key
    ```
*   **Option B (Environment Variable):**
    *   Set the `OPENAI_API_KEY` environment variable:
    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```

---

## 🗂️ Project Structure
```
JARVIS-AI-with-OpenAI-main
    ├── main.py # Primary script for Jarvis AI
    ├── main2.py # Secondary script
    ├── config.py # Configuration file for API key
    ├── requirements.txt # Dependencies
    ├── Openai/ # Folder for storing AI responses
    ├── music/ # Music files used by the assistant
    └── audio.wav # Placeholder for audio input/output
```


---

## 🚀 Usage

### 🏃 Run the Assistant

To start Jarvis AI, execute:

```bash
python main.py
```

### 🗣️ Commands
Here are some of the commands Jarvis understands:
- **Open [website]**: Opens specified websites like YouTube, Google, etc.
- **Play [music name] music**: Plays the specified music file.
- **What's the time?**: Provides the current time.
- **AI [your question]**: Queries the OpenAI API for a response.

---

## 📜  File Descriptions

### `main.py`
This is the primary script that:
- Initializes the Jarvis AI interface.
- Handles voice input and text commands.
- Integrates with OpenAI's API for intelligent responses.

### `main2.py`
Contains additional or secondary functionalities for the assistant. Can be customized or extended as needed.

---

## 🤝 Contributing
1. 🍴 Fork the repository.
2. 🌿 Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. ✍️ Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. 🚀 Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. 📤 Create a pull request.

---

## 📄 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⚠️ Troubleshooting
If you encounter issues during setup or execution:
1. Ensure all dependencies are installed.
2. Verify the API key in `config.py` or as an environment variable.
3. Refer to OpenAI's [API documentation](https://platform.openai.com/docs) for further guidance.
