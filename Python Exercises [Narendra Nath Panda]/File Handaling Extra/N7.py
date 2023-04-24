def read_txt(path):
        """read txt

        :return: <list>
        """        
#        path = "C:\Users\NARENDRA\Desktop\New folder\playway.txt"
        with open(path, "r", encoding='UTF-8') as f:
            txts = f.readlines()
        # remove chomp, blank
        sents = [item.strip().split(' ')[-1] for item in txts if len(item) > 1]
        return sents 