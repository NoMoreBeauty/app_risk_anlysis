import os
from langchain_community.llms import Tongyi
from langchain_core.messages import HumanMessage, SystemMessage 

os.environ["DASHSCOPE_API_KEY"] = "sk-7daf40f436cc48dfa96b5367f78cd419"

def get_prompt(prompt_path:str)->str:
    with open(prompt_path, 'r', encoding='utf-8') as fin:
        prompt = fin.read()
        # print(prompt)
        fin.close()
    return prompt

def create_llm(model = 'tongyi'):
    if model == 'tongyi':
        llm = Tongyi()
        return llm

def comments_sum(path1 = '/Users/wangjh/workspace/app_risk_anlysis/modules/评论处理/prompt_template.txt', data = ''):
    prompt = get_prompt(path1)
    # data = get_prompt('/Users/wangjh/workspace/app_risk_anlysis/modules/评论处理/data_positive.txt')
    prompt = prompt + data
    llm = create_llm()
    message = [
    SystemMessage(prompt),
    # HumanMessage("请你帮我生成一份存在权限滥用风险应用的manifest文件"),
    ]
    response = llm.invoke(message)
    return response

if __name__ == '__main__':
    comments_sum()