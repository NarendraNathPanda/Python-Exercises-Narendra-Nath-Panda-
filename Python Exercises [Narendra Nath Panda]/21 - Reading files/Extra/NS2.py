def readGenomeSizeFromTxt(fname):
    """
    Read genome information.
    
    Args:
    -----
        fname: a txt file contains genome information

    Returns:
    -----
        A dictionary contains SQ as key and SL as value, otherwise None
    """
    # first check if fname is a bam file
    res = dict();
    with open(fname) as fin:
        for line in fin:
            elems = line.split();
            chr_name = elems[0];
            chr_len = int(elems[1]);
            res[chr_name] = chr_len;
    return res 