# encoding: utf-8
__author__ = 'yeayee'
from mongo import Mongodb
db_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'test_mongo'
}
test_date = [
    {
        '_id': 1,
        'id': 1,
        'name': 'Lily',
        'sex': 'F',
        'age': 20,
        'city': 'shanghai',
        'skill': ['word', 'excel']
    },
    {
        '_id': 2,
        'id': 2,
        'name': 'Tom',
        'sex': 'M',
        'age': 22,
        'city': 'shanghai',
        'skill': ['php', 'java']
    },
    {
        '_id': 3,
        'id': 3,
        'name': 'Jerry',
        'sex': 'M',
        'age': 22,
        'city': 'beijing',
        'skill': ['php', 'python']
    }
]
def test():
    try:
        table_name = 'user'
        conn = Mongodb(db_config)
        print(conn.db)
        print(conn.find_one(table_name))
        print(conn.remove(table_name))   # 清空记录
        print(conn.insert(table_name, test_date))   # 插入记录
        print(conn.distinct(table_name, 'age'))   # 统计年龄范围
        print(conn.update(table_name, {'id': 3}, {'age': 24}))   # id=3的记录年龄更新为24
        print(conn.distinct(table_name, 'age'))   # 统计年龄范围
        conn.output_rows(table_name)
        print(conn.update(table_name, {}, {'age': 1}, 'inc'))   # 所有记录年龄增加1岁
        conn.output_rows(table_name)
        # print(conn.update(table_name, {'id': 3}, {'skill': 'mysql'}, 'push'))  # 向数组字段中添加单个元素
        # print(conn.update(table_name, {'id': 3}, {'skill': 'mysql'}, 'pull')) # 向数组字段中删除单个元素
        print(conn.update(table_name, {'id': 3}, {'skill': ['ruby', 'c#']}, 'pushAll'))  # 向数组字段中添加多个元素
        print(conn.update(table_name, {'id': 3}, {'skill': ['ruby', 'c#']}, 'pullAll'))   # 向数组字段中删除多个元素
        conn.output_rows(table_name)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    test()



