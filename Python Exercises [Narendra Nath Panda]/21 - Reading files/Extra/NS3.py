def read_grnd_distri_from_txt(load_path):
    grnd_distri_list = []
    k = 0
    with open(load_path, 'r') as fd:
        for line in fd:
            # print scale_distri_list[k], line, line.split()
            # exit()
            tmp_vec = [torch.FloatTensor([float(x)]) for x in line.split()]
            # print 'before concat: ', tmp_vec
            tmp_vec = torch.cat(tmp_vec)
            # print 'after concat: ', tmp_vec
            assert abs((1 - tmp_vec.sum())) < 0.1
            grnd_distri_list.append(tmp_vec)
            # print tmp_vec, scale_distri_list[k]
            # k += 1
            # if k == 2:
            #     exit()

    return grnd_distri_list 