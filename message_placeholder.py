from langchain_core.prompts import MessagePlaceholder, ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# chat template

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant.'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human', '{query}'),
])

# load chat history
chat_history_content = []
with open('chat_history.txt', 'r') as file:
    chat_history_content.append(file.readlines()) 

print(chat_history_content)

# chat prompt

chat_prompt = chat_template.invoke({
    'chat_history': chat_history_content,
    'query':'Where is my refund?',
})

print(chat_prompt)