def read_files():
    dict_files = {}
    for i in range(3):
        file_name = str(i + 1) + '.txt'
        with open(file_name, encoding='utf8') as f:
            file_ = f.readlines()
            qty_line = len(file_)
        file_ = [line.rstrip() for line in file_]
        dict_files[qty_line] = {'name': file_name, 'content': file_}
    return dict_files

def concatenation_files(dict_files):
    with open('result.txt', 'w', encoding='utf8') as f:
        for file_ in sorted(dict_files.items()):
            f.write(file_[1]['name'] + '\n')
            f.write(str(file_[0]) + '\n')
            f.writelines([l + '\n' for l in file_[1]['content']])
    return dict_files

if __name__ == '__main__':
    concatenation_files(read_files())