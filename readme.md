<div align="center">

# 🚀 LangChain MCP Client with Gemini 2.0

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/🦜🔗_LangChain-FFFFFF?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**A lightweight, powerful Python client bridging the Model Context Protocol (MCP) with LangChain and Google's lightning-fast Gemini 2.0 Flash model.**

</div>

---

Instantly turn any standalone MCP server (Python or Node.js) into a fully interactive, tool-using AI agent directly from your terminal!

## ✨ Features

* **🤖 Powered by Gemini 2.0:** Utilizes Google's latest `gemini-2.0-flash` model for incredibly fast and intelligent reasoning.
* **🔌 Plug-and-Play MCP:** Connects to any standard MCP server via `stdio` transport. Supports both Python (`.py`) and Node (`node`) servers automatically.
* **🛠️ Dynamic Tool Discovery:** Seamlessly uses `langchain_mcp_adapters` to detect, load, and bind tools from your server to the LangChain agent.
* **💬 Interactive REPL:** A clean, persistent terminal loop allowing you to chat with your agent, issue commands, and view formatted JSON responses.

## 📦 Prerequisites

* Python 3.9+
* A valid Google Gemini API Key

## 🛠️ Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

**2. Create a virtual environment (recommended):**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```
*(Installs `langchain`, `langchain_mcp_adapters`, `langchain_google_genai`, `google_generativeai`, and `python-dotenv`.)*

**4. Set up your environment variables:**
Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY="your_api_key_here"
```

## 🚀 Usage

Run the client script and pass the absolute or relative path to the target MCP server you want the agent to control.

```bash
python langchain_mcp_servers.py "/path/to/your/mcp_server.py"
```

Once connected, you will see:  
`🚀 MCP CLIENT STARTED! Type 'quit' to exit.`

### 💡 Example Interaction

```text
Query: "Run a single terminal command to create a file named success.txt with the text 'It works!' inside it."

Response:
{
  "type": "AgentFinish",
  "content": "I have successfully created the file `success.txt` with the text 'It works!' in the current workspace."
}
```

## 🏗️ How it Works under the hood

1. **Initialization:** The script spins up an `stdio` client to talk to the target server path provided in the CLI arguments.
2. **Tool Extraction:** It initializes the session and pulls available tools using LangChain's MCP adapter.
3. **Agent Binding:** A LangChain Agent is created, bonding the `gemini-2.0-flash` LLM with the server's tools.
4. **Execution:** User prompts are processed by Gemini, which decides if/when to call tools, executes them on the server, and returns human-readable results.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

This project is licensed under the [MIT License](LICENSE).