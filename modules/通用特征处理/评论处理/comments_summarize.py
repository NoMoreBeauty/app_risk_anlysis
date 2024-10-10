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

def comments_sum(path1 = '/Users/wangjh/workspace/app_risk_anlysis/modules/通用特征处理/评论处理/prompt_template.txt', data = ''):
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
    r = comments_sum(data='''1. 名称和图标太像，下载后才发现是仿冒。
2. 这款应用宣传不实，功能与描述完全不符。
3. 下载后看到不适当内容，体验极差，真让人失望。
4. 使用后发现有广告弹窗，体验不佳。
5. 应用收集了我的个人信息，感觉不安全。
6. 界面不友好，操作起来很麻烦。
7. 频繁崩溃，根本无法使用。
8. 付款后没得到任何服务，像是被骗了。
9. 内容更新慢，很多功能都没用。
10. 论坛里的评论虚假，大家注意了！
''')
    print(r)