# 🤖 Assistant Chatbot

A simple yet powerful chatbot application powered by **Llama 3.2** and **Ollama**, with a modern web interface built using **Streamlit**.

## Features

- 💬 **Real-time Streaming Responses** - See responses generated character by character
- 🎨 **Modern Web UI** - Sleek Streamlit interface with chat history
- ⚙️ **Customizable Settings** - Adjust temperature and system prompts
- 📝 **Conversation Context** - Maintains chat history for context-aware responses
- 🗑️ **Clear History** - Reset conversations with one click
- ⚡ **Fast & Efficient** - Runs locally using Ollama

## Requirements

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model downloaded

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abdalhafez006/Assistant-chat-bot.git
   cd Assistant-chat-bot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Llama 3.2 model:**
   ```bash
   ollama pull llama3.2:latest
   ```

## Usage

### Streamlit Web Interface (Recommended)
```bash
streamlit run streamlit_app.py
```
Then open your browser to `http://localhost:8501`

**Sidebar Options:**
- 🌡️ **Temperature** - Control response creativity (0.0 = focused, 1.0 = creative)
- 📝 **System Prompt** - Define the assistant's behavior
- 🗑️ **Clear Chat History** - Reset the conversation

### Terminal Chatbot
```bash
python app.py
```
Type your messages and interact with the chatbot directly in the terminal. Type `exit` or `quit` to end the conversation.

## Project Structure

```
.
├── streamlit_app.py      # Main Streamlit web application
├── app.py                # Terminal-based chatbot
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Technologies Used

- **Llama 3.2** - AI language model
- **Ollama** - Local AI model runner
- **Streamlit** - Web UI framework
- **Python 3.13** - Programming language

## Requirements

See [requirements.txt](requirements.txt) for the complete list of dependencies.

## Getting Started

1. Make sure Ollama is running (`ollama serve`)
2. Ensure Llama 3.2 model is downloaded
3. Run the Streamlit app: `streamlit run streamlit_app.py`
4. Start chatting!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Created with ❤️ for AI enthusiasts**
