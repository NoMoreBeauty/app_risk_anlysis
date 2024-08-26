import json
from typing import List

def get_permission_score_llm(outliers:str, risk_list:dict)->float:
    outliers_js = json.loads(outliers)
    risk_score = 0
    for p in outliers_js['过渡申请的权限']:
        risk_score += risk_list[p['权限类别']]

    return risk_score

if __name__ == '__main__':
    outlilers = '''
{
  "过渡申请的权限": [
    {
      "权限名称": "READ_CONTACTS",
      "权限类别": "危险权限"
    },
    {
      "权限名称": "RECORD_AUDIO",
      "权限类别": "危险权限"
    },
    {
      "权限名称": "ACCESS_FINE_LOCATION",
      "权限类别": "危险权限"
    },
    {
      "权限名称": "SEND_SMS",
      "权限类别": "危险权限"
    },
    {
      "权限名称": "WRITE_SECURE_SETTINGS",
      "权限类别": "特权权限"
    }
  ]
}
'''
    risk_list = {
        '正常权限' : 0.1,
        '危险权限' : 2,
        '特权权限' : 10,
        '签名权限' : 10,
    }
    risk_score = get_permission_score_llm(outliers=outlilers, risk_list=risk_list)
    print(risk_score)