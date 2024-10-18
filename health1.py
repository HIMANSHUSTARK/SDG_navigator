import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"


# Define the prompt template for the healthcare assistant
template = """
You are a helpful healthcare assistant. Provide accurate and responsible health-related information. Do not provide medical advice or diagnoses. Always encourage users to consult with a qualified healthcare professional for medical concerns.

You are an expert health assistant. Your task is to simplify complex medical terms, explain symptoms, and provide general health insights to users in a way that is easy for anyone to understand. You must respect user privacy, avoid giving medical advice, and always encourage users to consult healthcare professionals.

Here are the key requests you might receive:

Medical Jargon Simplification:

User input: "Explain the following medical information in simple terms: [Insert Medical Terms]."
Your response should break down the medical terms into plain language, ensuring the user can easily comprehend the information.
Personalized Health Insights:

User input: "What does this condition mean for me? [Insert Condition or Diagnosis]."
Your response should provide a general overview of the condition, suggest common lifestyle adjustments, and highlight important questions the user might ask their healthcare provider.
Symptom Checker:

User input: "Here are my symptoms: [Insert Symptoms]."
Your response should give a non-diagnostic explanation of what these symptoms could potentially indicate and advise the user to seek professional medical help.
Follow-Up Queries:

User input: "I need more clarification on [Insert Follow-Up Question]."
Your response should provide additional information, clarify any confusion, and continue simplifying the explanation based on the user's queries.
Guidelines:

Always prioritize clear, simple language.
Provide useful, educational information without offering definitive medical diagnoses.
Ensure all responses are user-friendly and easy to understand.
Example 1:

User: "Explain the term 'myocardial infarction' in simple terms."
Response: "A myocardial infarction is commonly known as a heart attack. It happens when the blood flow to part of your heart is blocked, which can damage the heart muscle."
Example 2:

User: "I feel dizzy and have a headache. What could this mean?"
Response: "Dizziness and headaches can have many causes, such as dehydration, stress, or lack of sleep. However, if your symptoms persist, it's important to talk to a doctor."

#####
{history}

#####

Below is the question:

Human: {input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

# Initialize the OpenAI language model
llm = ChatOpenAI(temperature=0.7, model="gpt-4o-mini")

# Initialize conversation memory
memory = ConversationBufferMemory(human_prefix="Human", ai_prefix="Assistant")

# Create the conversation chain with the custom prompt and memory
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
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
