def read_txt_into_list(txtfile):
    with open(txtfile, 'r') as f:
        content = f.readlines()
        eventlist = [ line.rstrip() for line in content]
    return eventlist 