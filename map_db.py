import os
import json
import sqlite3


def map_data():
    with open('file_list.json', 'r', encoding='utf-8') as f:
        json_text = f.read()
    file_list = json.loads(json_text)
    sql = "insert into source_map ('s_name','s_index','s_path','s_category') values ('{name}','{index}','{path}'," \
          "'{category}') "
    with sqlite3.connect('sources.db') as conn:
        cursor = conn.cursor()
        cursor.executescript('''delete from source_map;
        update sqlite_sequence SET seq = 0 where name = 'source_map';''')
        for s in file_list:
            cursor.execute(sql.format(name=s[0], index=s[1], path=s[2], category=s[3]))
            print(s)
        conn.commit()
        cursor.close()
        file_list.clear()


if __name__ == "__main__":
    map_data()
