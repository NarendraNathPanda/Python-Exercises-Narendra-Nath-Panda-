def ReadLmkFromTxtRecursive(path,format):
    ct = 0
    list = []
    for root, dirs, files in os.walk(path):
        for fold in dirs:
            files = os.listdir(root+fold)
            for file in sorted(files):
                if file.endswith(format):
                    lmk = np.loadtxt(root+fold+'/'+file) # 68x2
                    n,d = lmk.shape
                    lmk = lmk.reshape((n*d))
                    list.append(lmk)
                    ct = ct + 1
                    if ct == 10000:
                        return list
    return list 