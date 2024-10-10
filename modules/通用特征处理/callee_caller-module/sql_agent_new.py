import sqlite3
import os
from langchain_community.llms import Tongyi

from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import tool

conn = sqlite3.connect('./database/demo.db')
cursor = conn.cursor()
os.environ["DASHSCOPE_API_KEY"] = "sk-8461d57af4954b3f82e20b589b7c58c7"
llm = Tongyi()

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
        return results
    except Exception as e:
        return str(e)
    
def create_agent(template, llm):
    prompt = PromptTemplate.from_template(template)
    tools = [execute_sql_query]
    agent = create_react_agent(llm, tools, prompt)
    return agent

if __name__ == '__main__':
    template = '''
        Answer the following questions in Chinese as best you can. 
        Try to answer the question by yourself.
        If not necessary, don't use the tools.
        You have access to the following tools:{tools}
        Use the following format:
        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question
        Begin!
        Question: {input}
        Thought:{agent_scratchpad}
        '''
    agent = create_agent(template=template, llm=llm)

    agent_executor = AgentExecutor(agent=agent, tools=[execute_sql_query], max_iterations = 10,handle_parsing_errors=True,verbose= True)

    # result = agent_executor.invoke({'input' : 'student表中有多少名学生，且名字是什么？'})
    result = execute_sql_query.invoke('SELECT COUNT(*), name FROM student')
    print(result)