import simplejson as json # 需要先通过pip install simplejson来安装它才可以用,python3中需要使用这个，没有json库了
# 程序主入口
if __name__ == "__main__":
    """解读字符串拼装成json写入文件，方便其他语言解析数据"""
    file_path = '../resources/json.txt'
    file_obj = open(file_path, "r", encoding='UTF-8')
    all_lines = file_obj.readlines()
    data = {}
    key_value = 0
    for line in all_lines:
        line_info = line.split(',')
        if line_info:
            info = {"name": line_info[0], "url": line_info[1].replace("\n", "")}
            data[key_value] = info
            key_value += 1
    file_obj.close()
    file = open('../resources/json.json', 'w', encoding='utf-8')
    json.dump(data, file, ensure_ascii=False)