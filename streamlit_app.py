import streamlit as st
import ollama

MODEL_NAME = "llama3.2:latest"

# Set page config
st.set_page_config(
    page_title="Assistant Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Assistant Chatbot")
st.write("Chat with Assistant powered by Ollama")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher values = more creative, Lower values = more focused"
    )
    
    # System prompt
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful assistant.",
        height=100,
        help="Define the behavior of the assistant"
    )
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # About section
    st.divider()
    st.write("### About")
    st.write("Powered by Llama 3.2 and Ollama")
    st.write("Built with Streamlit")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful assistant."

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Say something..."):
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Prepare messages with system prompt
            messages_with_system = [
                {
                    "role": "system",
                    "content": system_prompt
                }
            ] + st.session_state.messages
            
            # Stream response from Ollama
            stream = ollama.chat(
                model=MODEL_NAME,
                messages=messages_with_system,
                stream=True,
                options={
                    "temperature": temperature
                }
            )
            
            # Stream chunks and display in real-time
            for chunk in stream:
                full_response += chunk['message']['content']
                message_placeholder.markdown(full_response + "▌")
            
            # Final message without cursor
            message_placeholder.markdown(full_response)
            
            # Add assistant response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response
            })
            
        except Exception as e:
            st.error(f"Error: {e}")
            # Remove user message if there was an error
            st.session_state.messages.pop()
