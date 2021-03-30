import os
import json

file_list = []


def get_file_list(root):
    list_path = os.listdir(root)
    for i in range(0, len(list_path)):
        path = os.path.join(root, list_path[i])
        if os.path.isfile(path):
            file_name = os.path.basename(path)
            if file_name.find('.py') > 0 or file_name.find('.db') > 0 or file_name.find('.json') > 0:
                continue
            file_path = path.replace("\\", "/")
            if '.mdb' in file_name:
                if '_jp' in file_name:
                    index = 22222
                    category = 'master'
                    set_result(file_name, index, file_path, category)
                if '_cn' in file_name:
                    index = 22221
                    category = 'master'
                    set_result(file_name, index, file_path, category)
                if '_kr' in file_name:
                    index = 22220
                    category = 'master'
                    set_result(file_name, index, file_path, category)
                continue
            if '.txt' in file_name:
                if '_jp' in file_name:
                    index = 11112
                    category = 'db_version'
                    set_result(file_name, index, file_path, category)
                if '_cn' in file_name:
                    index = 11111
                    category = 'db_version'
                    set_result(file_name, index, file_path, category)
                if '_kr' in file_name:
                    index = 11110
                    category = 'db_version'
                    set_result(file_name, index, file_path, category)
                continue
            strs = file_name.replace(".png", "").split("_")
            if 'train' in file_name:
                try:
                    index = int(strs[3])
                except:
                    index = int(strs[4])
                print(file_name)
                if 'trained_chr_icon' in file_name:
                    try:
                        category = 'trained_chr_icon' + f'_{strs[4]}_' + f'{strs[5]}'
                    except:
                        category = 'trained_chr_icon'
                elif 'chr_icon_training' in file_name:
                    category = 'chr_icon_training'
                elif 'mob' in file_name:
                    category = f'trained_mob_chr_icon_{strs[5]}_{strs[6]}'
                print(category)
            else:
                try:
                    index = int(strs[2])
                except:
                    try:
                        index = int(strs[3])
                    except:
                        index = 0
                if len(strs) > 4:
                    category = strs[0] + f'_{strs[1]}_' + f'{strs[3]}_' + f'{strs[4]}'
                elif len(strs) == 4:
                    if 'card' in file_name:
                        category = strs[0] + f'_{strs[1]}_' + f'{strs[2]}'
                    else:
                        category = strs[0] + f'_{strs[1]}_' + f'{strs[3]}'
                elif len(strs) <= 3:
                    if file_name.find('item_random') > 0:
                        category = 'item_random'
                    else:
                        category = strs[0] + f'_{strs[1]}'
            set_result(file_name, index, file_path, category)
        else:
            get_file_list(path)


def set_result(file_name, index, file_path, category):
    result_set = (file_name, index, file_path, category)
    file_list.append(result_set)


def write_list():
    json_obj = json.dumps(file_list, ensure_ascii=False)
    with open('./file_list.json', 'w+', encoding='utf-8') as f:
        f.write(json_obj)


if __name__ == '__main__':
    get_file_list(os.getcwd())
    write_list()
