import json
import os
import analyse


def create_dirs(file_types):
    for path in file_types:
        if not os.path.exists(f'./scripts/{path}'):
            os.makedirs(f'./scripts/{path}')


def create_scripts(file_types):
    for file_type in file_types:
        script_text = f'''import sqlite3
import shutil
import json
          
            
def get_files():
    sql = "select n,h from a where m = '{file_type}'"
    conn = sqlite3.connect('../../meta')
    cursor = conn.cursor()
    result = cursor.execute(sql).fetchall()
    cursor.close()
    conn.close()
    miss_list = []
    for result_set in result:
        file_name_lst = result_set[0].split('/')
        file_name = file_name_lst[len(file_name_lst) - 1]
        file_ori_name = result_set[1]
        fir_dir = file_ori_name[0:2]
        try:
            shutil.copy(f'../../dat/{{fir_dir}}/{{file_ori_name}}', f'./{{file_name}}')
        except:
            miss_list.append(file_ori_name)
    if len(miss_list) > 0:
        json_obj = json.dumps(miss_list, ensure_ascii=False)
        with open('./miss_list.json', 'w+', encoding='utf-8') as f:
            f.write(json_obj)
        miss_list.clear()    

    
if __name__ == '__main__':
    get_files()'''
        with open(f'./scripts/{file_type}/script.py', 'w+', encoding='utf-8') as f:
            f.write(script_text)
        with open(f'./scripts/{file_type}/run.bat', 'w+', encoding='utf-8') as b:
            b.write('''python script.py
pause''')


if __name__ == '__main__':
    if not os.path.exists('./config/fileTypes.json'):
        analyse.get_file_types('meta')
    with open('config/fileTypes.json', 'r', encoding='utf-8') as f:
        file_types = json.load(f)
    create_dirs(file_types=file_types)
    create_scripts(file_types=file_types)
