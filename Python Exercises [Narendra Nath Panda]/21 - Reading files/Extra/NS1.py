def read_column_data_from_txt(fname):
    """
    Read data from a simple text file.

    Format should be just numbers.
    First column is the dependent variable. others are independent.
    Whitespace delimited.

    Returns
    -------
    x_values : list
        List of x columns
    y_values : list
        list of y values

    """
    datafile = open(fname)
    datarows = []
    for line in datafile:
        datarows.append([float(li) for li in line.split()])
    datacols = list(zip(*datarows))
    x_values = datacols[1:]
    y_values = datacols[0]

    return x_values, y_values 