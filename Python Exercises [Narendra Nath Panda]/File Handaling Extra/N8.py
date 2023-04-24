def read_txt(inputfiles):
    p1 = r"(.*)[0-9](.*?).*"
    temp_list = []
    with open(inputfiles,'r',encoding='gbk') as f:
        for line in f:
            mathObj = re.match(p1,line)
            if mathObj:
                line = line.strip()
                temp_list.append(line)
    return temp_list 