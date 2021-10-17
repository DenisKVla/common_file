import os

def get_lens_of_files():
    os.chdir("test")
    dir = os.getcwd()
    list_files = os.listdir(dir)
    info_dict = []
    for item in list_files:
        with open(item, encoding="UTF-8") as file:
            count_str = len(file.readlines())
            info_dict.append({'name': item,'len':count_str})

    info_dict.sorted(info_dict['len'])
    return info_dict


print(get_lens_of_files())
#def write_to_common_file(filename):

