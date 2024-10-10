import json
from nodeA.node import mainA

def read_test_data(path:str):
    with open(path, 'r') as fin:
        data = json.load(fin)
    return data

if __name__ == '__main__':
    data = read_test_data('/Users/wangjh/workspace/app_risk_anlysis/modules/决策树/应用信息风险/test_data.json')
    nodeA_result = mainA(data=data)