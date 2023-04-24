def read_txt_file(file_name):
  """ Read the data inside a file to a dictionary """

  data_dict = {}
  key_list = []

  with open(file_name, "r") as file:
    for count, line in enumerate(file):
      # the first line should contain the key of each column
      if count == 0:
        key_list = line.split()
        num_key = len(key_list)
        for key in key_list:
          data_dict[key] = []
      else:
        token_list = line.split()

        if len(token_list) < num_key:
          # sanity check
          logger.warning("There are missing tokens")
          # handle corner cases (missing token) in node file
          data_dict[key_list[0]].append(token_list[0])
          data_dict[key_list[1]].append("missing_token")
          data_dict[key_list[2]].append(token_list[1])
          # print("file_name = {}".format(file_name))
          # raw_input("wait")
        elif len(token_list) > num_key:
          logger.warning("There is something wrong!")
          logger.warning("file name = {}".format(file_name))
          raw_input("wait")
        else:
          for idx, token in enumerate(token_list):
            data_dict[key_list[idx]].append(token)

  return data_dict 