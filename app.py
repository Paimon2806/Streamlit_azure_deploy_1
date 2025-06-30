from langchain.chat_models import AzureChatOpenAI
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize the Azure Chat Model
llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_API_BASE"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model_name="gpt-4o",
    temperature=0.7,
)

st.title("Azure OpenAI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Callback to handle user input
def handle_input():
    user_input = st.session_state["user_input"]
    if user_input:
        response = llm.invoke(user_input)
        st.session_state.messages.append({
            "user": user_input,
            "bot": response.content
        })
        st.session_state["user_input"] = ""  # Clear input safely

# Display previous messages
for msg in st.session_state.messages:
    st.write(f"**You:** {msg['user']}")
    st.write(f"**Bot:** {msg['bot']}")

# Input with callback
st.text_input("You:", key="user_input", on_change=handle_input)
