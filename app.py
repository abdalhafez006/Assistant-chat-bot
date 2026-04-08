import ollama

MODEL_NAME = "llama3.2:latest"

def chatbot():
    """Simple chatbot using Llama 3.2 via Ollama"""
    print("🤖 Llama 3.2 Chatbot")
    print("Type 'exit' or 'quit' to end the conversation\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get streaming response from Llama 3.2
            print("\nBot: ", end="", flush=True)
            full_response = ""
            
            stream = ollama.chat(
                model=MODEL_NAME,
                messages=conversation_history,
                stream=True
            )
            
            # Stream the response chunks
            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                print(content, end="", flush=True)
            
            print("\n")  # New line after response
            
            # Add assistant response to history
            conversation_history.append({
                "role": "assistant",
                "content": full_response
            })
            
        except Exception as e:
            print(f"\nError: {e}")
            # Remove the last user message if there was an error
            conversation_history.pop()

if __name__ == "__main__":
    chatbot()


