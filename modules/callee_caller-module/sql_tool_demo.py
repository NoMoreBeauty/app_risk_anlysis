import sqlite3

def create_table():
    conn = sqlite3.connect('./database/app-states.db')
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists apptable(
            id integer primary key autoincrement not null,
            app_id text,
            app_description text
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_data():
    conn = sqlite3.connect('./database/app-states.db')
    cursor = conn.cursor()
    # data = [
    #     (1, 'app-3208', 'app-3208是一款运动记录应用，因为过度广告问题已于2023年1月5日下架。'),
    #     (2, 'app-9728', 'app-9728是一款心率监控与分析的应用，目前上架中。'),
    #     (3, 'app-3210', 'app-3210是一款电子社交应用，目前上架中。'),
    #     (4, 'app-8310', 'app-8310是一款电子支付应用，目前上架中。'),
    # ]
    data = (3, 'app-3210', 'app-3210是一款电子社交应用，目前上架中。')
    sql = 'insert into apptable values (?, ?, ?)'
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

def select_data():
    conn = sqlite3.connect('./database/app-states.db')
    cursor = conn.cursor()
    sql = 'select * from apptable'
    cursor.execute(sql)
    for item in cursor:
        print(item)
    conn.commit()
    cursor.close()
    conn.close()


def update_data():
    conn = sqlite3.connect('./database/app-states.db')
    cursor = conn.cursor()
    sql = "update student set name = 'mary' where name = 'john'"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # create_table()
    # select_data()
    # insert_data()
    select_data()