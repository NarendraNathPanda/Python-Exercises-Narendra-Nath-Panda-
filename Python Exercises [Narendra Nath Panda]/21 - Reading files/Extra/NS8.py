def readTxt(txt_path):
    objs = []
    with open(txt_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip('\ufeff')
        line = line.strip('\n')
        bbox, text = line.split(',')[:8], line.split(',')[-1]

        bbox = [int(coord) for coord in bbox]

        anno = {'category_id': 1, 'bbox': bbox, 'text': text, \
                'isDifficult': 1 if text=='###' else 0}
        objs.append(anno)
    return objs 