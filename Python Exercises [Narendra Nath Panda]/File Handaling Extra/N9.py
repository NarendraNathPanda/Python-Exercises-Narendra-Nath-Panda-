def read_txt(file_name):
    txt_data = []
    with open(file_name, 'r', encoding='utf8') as f:
        d = f.readline()
        while d:
            txt_data.append(d.strip())
            d = f.readline()
    return txt_data