import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain import ConversationChain
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"


# Define the prompt template for the healthcare assistant
template = """
You are a helpful healthcare assistant. Provide accurate and responsible health-related information. Do not provide medical advice or diagnoses. Always encourage users to consult with a qualified healthcare professional for medical concerns.

{history}
Human: {input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Initialize the OpenAI language model
llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

# Create the conversation chain with the custom prompt
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    verbose=False
)

# Streamlit app
def main():
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="🩺")
    st.title("🩺 Healthcare Chatbot")
    st.write("Welcome to the Healthcare Chatbot. How can I assist you today?")

    # Initialize session state variables
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "history" not in st.session_state:
        st.session_state.history = ""

    # Display chat history using Streamlit's chat messages
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            with st.chat_message("user"):
                st.markdown(message)
        else:
            with st.chat_message("assistant"):
                st.markdown(message)

    # Input area using st.chat_input
    user_input = st.chat_input("Type your message here...")
    if user_input:
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate and display assistant's response
        response = conversation.predict(input=user_input)
        with st.chat_message("assistant"):
            st.markdown(response)

        # Update conversation history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Assistant", response))
        st.session_state.history += f"Human: {user_input}\nAssistant: {response}\n"

    # Option to save chat history
    if st.button("Save Chat History"):
        save_chat_history()

def save_chat_history():
    import time
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    history_filename = f"chat_history_{timestamp}.txt"
    chat_history_text = ""
    for speaker, message in st.session_state.chat_history:
        chat_history_text += f"{speaker}: {message}\n"
    with open(history_filename, "w", encoding="utf-8") as f:
        f.write(chat_history_text)
    st.success(f"Chat history saved to {history_filename}")

if __name__ == "__main__":
    main()
