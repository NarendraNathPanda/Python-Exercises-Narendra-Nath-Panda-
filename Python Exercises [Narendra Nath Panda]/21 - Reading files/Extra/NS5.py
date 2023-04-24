def read_txt_vectors(path):
    """ Read vectors file in text format. This code expects correct format of input file.

        Args:
            path (string_types): path to txt file

        Returns:
            Dict[np.array]: name to array mapping
    """
    data_dict = {}
    with open(path) as f:
        for line in f:
            splitted_line = line.split()
            name = splitted_line[0]
            end_idx = splitted_line.index(']')
            vector_data = np.array([float(single_float) for single_float in splitted_line[2:end_idx]])
            data_dict[name] = vector_data
    return data_dict 