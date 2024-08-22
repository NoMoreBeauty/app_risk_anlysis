import os
from utils.prompt_tool import get_prompt
from langchain_community.llms import Tongyi
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

os.environ["DASHSCOPE_API_KEY"] = "sk-8461d57af4954b3f82e20b589b7c58c7"

llm = Tongyi()

prompt = get_prompt('./modules/permission-module/prompts/classification2.txt')
# print(prompt)
message = [
    SystemMessage(prompt),
    # HumanMessage("请你帮我生成一份存在权限滥用风险应用的manifest文件"),
]

response = llm.invoke(message)
print(response) # openai model will return AIMessage type answer which needs a parser
