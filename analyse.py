import sqlite3
import json
import os


def get_file_types(path):
    sql = 'select m from a group by m'
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        result_set = cursor.execute(sql)
        result = [res[0] for res in result_set]
        cursor.close()
    json_obj = json.dumps(result, ensure_ascii=False)
    if not os.path.exists('./config'):
        os.makedirs('./config')
    with open("config/fileTypes.json", "w+", encoding="utf-8") as f:
        f.write(json_obj)


if __name__ == '__main__':
    get_file_types('meta')
