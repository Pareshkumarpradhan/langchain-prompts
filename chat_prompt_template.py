from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()  # Load environment variables from .env file

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "explain in simple terms, what is {topic}?"),

    # SystemMessage(content="You are a helpful {domain} expert."),
    # HumanMessage(content="explain in simple terms, what is {topic}?"),
])

prompt = chat_template.invoke({
    "domain": "science",
    "topic": "quantum computing"
    })

response = model.invoke(prompt)
print("Response:", response.content)