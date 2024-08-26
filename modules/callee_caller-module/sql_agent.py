import sqlite3
import os
from langchain_community.llms import Tongyi
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import tool

conn = sqlite3.connect('./database/app-states.db')
cursor = conn.cursor()
os.environ["DASHSCOPE_API_KEY"] = "sk-8461d57af4954b3f82e20b589b7c58c7"

llm = Tongyi()

def get_prompt(prompt_path:str)->str:
    with open(prompt_path, 'r', encoding='utf-8') as fin:
        prompt = fin.read()
        # print(prompt)
        fin.close()
    return prompt


@tool
def execute_sql_query(sql_query):
    """
    输入的参数是sqlite3的sql查询语句，返回的结果是内容为元组的列表。
    """
    try:
        cursor.execute(sql_query)
        results = []
        for item in cursor:
            results.append(item)
        conn.commit()
        return results
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    tools = load_tools([], llm=llm)
    agent = initialize_agent(tools + [execute_sql_query], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt = get_prompt('./prompts/insert_app_states.txt')
    result = agent.invoke(prompt)
    print(result)