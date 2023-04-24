def read_txt_to_struct(fname):
    """
    read txt to structure, the column represents:
    [frame number] [identity number] [bbox left] [bbox top] [bbox width] [bbox height] [DET: detection score, GT: ignored class flag] [class] [visibility ratio]
    """
    data = []
    with open(fname, 'r') as fid:
        lines = fid.readlines()
        for line in lines:
            line = list(map(float, line.strip().split(',')))
            data.append(line)
    data = np.array(data)

    # change point-size format to two-points format
    data[:, 4:6] += data[:, 2:4]
    
    return data 