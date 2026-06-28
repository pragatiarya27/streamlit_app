# streamlit_app
%%writefile README.md
# AI Agent Toolkit

This repository contains a collection of Streamlit applications and LangChain agents designed to demonstrate various AI capabilities, including conversational AI, data analysis, and tool-use.

## Project Structure
- `app1.py`: An Agent Builder Streamlit app for configuring AI agent identity and behavior.
- 

## Features

- **Streamlit Web Applications**: Interactive web interfaces for AI demonstrations.
- **LangChain Integration**: Utilizes LangChain for building sophisticated AI workflows.
- **Groq API**: Leverages the Groq API for high-performance language model inference.
- **Tool Use**: Agents capable of using external tools like search and a calculator.
- **Reflection and Self-Critique**: Advanced agents that can refine their outputs based on feedback.

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd AI-Agent-Toolkit
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    (Assuming you have a `requirements.txt` or you can install individual packages:
    `pip install streamlit langchain-groq langchain-community ddgs pyngrok`)

3.  **Configure API Keys**:
    - Obtain a Groq API key from [Groq Console](https://console.groq.com/).
    - Store your API key securely (e.g., in Google Colab secrets or as an environment variable).

4.  **Run Streamlit applications**:
    To run any of the Streamlit apps, use the command:
    ```bash
    streamlit run <app_name>.py
    ```
    For example:
    ```bash
    streamlit run app1.py
    ```

    If running in a Colab environment and you want public access, you can use `pyngrok` as demonstrated in the notebook:
    ```python
    from pyngrok import ngrok
    import subprocess
    import time
    import os

    # Kill any running ngrok processes to free up previous tunnels
    os.system("killall ngrok")

    process=subprocess.Popen(
        ["streamlit","run","app1.py","--server.port","8504","--server.headless","true"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(3)
    public_url=ngrok.connect(8504)
    print(f"Your app is live at:{public_url}")
    ```

## Usage
- **`app1.py`**: Configure and preview AI agent prompts.
  - **LangChain Reflection Graphs**: Interact with the reflection and self-critique agents by invoking their respective `reflection_graph.invoke` calls in the notebook cells.
.
