import os

def get_lens_of_files():
    os.chdir("test")
    dir = os.getcwd()
    list_files = os.listdir(dir)
    info_dict = []
    for item in list_files:
        with open(item, encoding="UTF-8") as file:
            counter = 0
            data = ''
            for line in file:
                counter = counter + 1
                data = data + line
            info_dict.append({'name': item,'len': counter, 'data' : data})

    info_dict.sort(key = lambda d : d['len'])
    return info_dict

def write_to_common_file(filename, dict_wiht_date):
    with open(filename, "w") as file:
        for info in dict_wiht_date:
            file.write(info['name']+'\n')
            file.writelines(str(info['len'])+'\n')
            file.write(info['data']+'\n')


write_to_common_file('com.txt',get_lens_of_files())