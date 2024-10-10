# 名称或图标与其他应用过于相似，导致用户混淆或知识产权侵权
import yaml
import sys
import os
sys.path.append('/Users/wangjh/workspace/app_risk_anlysis/modules/评论处理')
# from comments_summarize import comments_sum

total_testing_items = 6
total_testing_items_names = ['ip_tort', 'counterfeit', 'hmogenization', 'hormonyUX', 'similarity', 'comment']
configs = None

def init(path:str):
    with open(path, 'r') as file:
        config_data = yaml.safe_load(file)
    global configs
    configs = config_data

def ip_tort(data)->bool:
    '''
    华为检测项：IP侵权
    '''
    if data['handle_code'] == None:
        return False
    elif data['handle_code'] in configs['ip_tort']:
        return True
    else:
        return False
    
def counterfeit(data)->bool:
    '''
    华为检测项：仿冒
    '''
    if data['handle_code'] == None:
        return False
    elif data['handle_code'] in configs['counterfeit']:
        return True
    else:
        return False
    
def hmogenization(data)->bool:
    '''
    华为检测项：同质化
    '''
    if data['handle_code'] == None:
        return False
    elif data['handle_code'] in configs['hmogenization']:
        return True
    else:
        return False
    
def hormonyUX(data)->bool:
    '''
    华为检测项：鸿蒙UX
    '''
    if data['handle_code'] == None:
        return False
    elif data['handle_code'] in configs['hormonyUX']:
        return True
    else:
        return False
    
def similarity(data)->bool:
    # TODO
    return True

def comment(data)->bool:
    cmt = data['comment']  # comment list
    ans = cmt.split(' - ')[0]
    if ans == '存在':
        return 1
    elif ans == '不存在':
        return 0

def similarity(data)->bool:
    '''
    自己设计的相似度（名称） Example
    '''
    # TODO
    pass

def mainA(data):
    init(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml'))
    results = [ 0 for _ in range(total_testing_items)]
    for i in range(total_testing_items):
            if total_testing_items_names[i] in globals():
                if globals()[total_testing_items_names[i]](data) == True:
                    results[i] = 1
            else:
                print("func name cannot be found in the testing items!")
    return results

if __name__ == '__main__':
    # x = mainA({'handle_code':'CGjh016' , 'comment':['应用收集了我的个人信息，感觉不安全。','界面不友好，操作起来很麻烦。','频繁崩溃，根本无法使用。','名称和图标太像，下载后才发现是仿冒。','这款应用宣传不实，功能与描述完全不符。']})
    # comments = comment({'handle_code':'CGjh016' , 'comment':['应用收集了我的个人信息，感觉不安全。','界面不友好，操作起来很麻烦。','频繁崩溃，根本无法使用。']})
    print(os.path.join(os.getcwd(), 'config.yaml'))
    # init('/Users/wangjh/workspace/app_risk_anlysis/modules/应用信息风险/node-A/config.yaml')
    # print(configs)