from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="gpt2",  # Using GPT-2 which supports text-generation
    task="text-generation",
    max_new_tokens=100,
    temperature=0.7,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

response = llm.invoke("What is the capital of India?")
print(response)

