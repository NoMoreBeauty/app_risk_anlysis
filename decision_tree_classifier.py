from typing import List
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from utils.data_pre_processing import get_benign_data
# X = [[0, 0, 1], [0, 0, 0], [1, 1, 1], [2, 2, 0], [2, 0, 1]]
# y = [0, 0, 1, 1, 0] 

# clf = DecisionTreeClassifier()

# clf.fit(X, y)

# prediction = clf.predict([[2, 0, 0]])  # 输入一条新的数据
# print(f'预测结果: {"进行户外活动" if prediction[0] == 1 else "不进行户外活动"}')

# tree.plot_tree(clf, filled=True)

def main(target_fields:List[str]):
    benign_data = get_benign_data(target_fields, 'benign.json')
    X = benign_data[:2]
    test_x = benign_data[-1]
    X = X + get_benign_data(target_fields, 'risky.json')
    Y = [0,0,1,1]
    clf = DecisionTreeClassifier()
    clf.fit(X, Y)

    prediction = clf.predict([test_x])  # 输入一条新的数据
    print(f'预测结果: {"良性应用" if prediction[0] == 0 else "风险应用"}')

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
    main(target_fields)

