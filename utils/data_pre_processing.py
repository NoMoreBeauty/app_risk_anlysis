import os
import json
from typing import List

def get_benign_data(required_fields:list, dataset_name:str)->List[int]:
    current_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(os.path.dirname(current_path))
    path = os.path.join(parent_dir, 'dataset', dataset_name)
    
    with open(path, 'r', encoding='utf-8') as fin:
        js_data = json.load(fin)
        fin.close()
    re_data = []
    for i in range(1, len(js_data) + 1):
        temp_list = []
        single_data = js_data[str(i)]
        for k in required_fields:
            temp_list.append(single_data[k])
        re_data.append(temp_list)
    return re_data

if __name__ == '__main__':
    target_fields = [
        "app_level_code",
        "app_status_code",
        # "virus_flag",
        "security_result",
        "user_score",
        "oper_score",
        "total_on_shelf_days",
        "avg_adv_score",
        "avg_tc_score",
        "avg_pe_score",
        "avg_qz_score",
        "avg_qp_score",
        "avg_db_score",
        "avg_zp_score",
        "load_file_path_unique",
        "emotion_rating",
        "malicious_score",
    ]
    x = get_benign_data(target_fields, 'benign.json')
    y = get_benign_data(target_fields, 'risky.json')
