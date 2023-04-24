def read_txt_matrix(path):
    """ Read features file in text format. This code expects correct format of input file.

    Args:
        path (string_types): path to txt file

    Returns:
        Dict[np.array]: name to array mapping
    """
    data_dict, name = {}, None
    with open(path) as f:
        for line in f:
            if '[' in line:
                name = line.split()[0] if len(line) > 3 else ''
                continue
            elif ']' in line:
                line = line.replace(' ]', '')
            assert name is not None, 'Incorrect format of input file `{}`.'.format(path)
            if name not in data_dict:
                data_dict[name] = []
            data_dict[name].append(np.fromstring(line, sep=' ', dtype=np.float32))
    for name in data_dict:
        data_dict[name] = np.array(data_dict[name])
    return data_dict 