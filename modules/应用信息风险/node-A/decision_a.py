# 名称或图标与其他应用过于相似，导致用户混淆或知识产权侵权
import yaml

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
    # TODO
    # 评论太多超出context size怎么处理

    cmt = data['comment']  # comment list
    cmt_total = ''
    for c in range(len(cmt)):
        temp_coment = f'第{c}条评论说：{cmt[c]}\n'
        cmt_total += temp_coment
    
    

def similarity(data)->bool:
    '''
    自己设计的相似度（名称） Example
    '''
    # TODO
    pass

def main(data):
    init('/Users/wangjh/workspace/app_risk_anlysis/modules/应用信息风险/node-A/config.yaml')
    results = [ 0 for _ in range(total_testing_items)]
    for i in range(total_testing_items):
            if total_testing_items_names[i] in globals():
                if globals()[total_testing_items_names[i]](data) == True:
                    results[i] = 1
            else:
                print("func name cannot be found in the testing items!")
    return results

if __name__ == '__main__':
    x = main({'handle_code':'CGjh016'})
    print(x)
    # init('/Users/wangjh/workspace/app_risk_anlysis/modules/应用信息风险/node-A/config.yaml')
    # print(configs)