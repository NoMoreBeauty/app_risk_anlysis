import sqlite3
import os
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import tool

os.environ["DASHSCOPE_API_KEY"] = "sk-7daf40f436cc48dfa96b5367f78cd419"
llm = Tongyi()

def get_prompt(prompt_path:str)->str:
    with open(prompt_path, 'r', encoding='utf-8') as fin:
        prompt = fin.read()
        # print(prompt)
        fin.close()
    return prompt

@tool
def execute_query(appid):
    """
    输入的参数是appid，返回的结果是一个内容是0或1的列表。
    """

    return [0,0,0,1,1]
    
def create_agent(template, llm):
    prompt = PromptTemplate.from_template(template)
    tools = [execute_query]
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
    agent_executor = AgentExecutor(agent=agent, tools=[execute_query], max_iterations = 10,handle_parsing_errors=True,verbose= True)

    prompt = get_prompt('/Users/wangjh/workspace/app_risk_anlysis/modules/应用信息风险/node-B/prompt.txt')
    result = agent_executor.invoke({'input' : prompt})
    # result = execute_query.invoke('app-3208')
    print(result)