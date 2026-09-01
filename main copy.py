from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load your .env file credentials
load_dotenv()

# Instantiate the chat model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Invoke the model with a direct prompt
response = llm.invoke("Give me a 3-word motivational motto.")

# Output the answer text
print(response.content)