def read_txt_file(read_file_path):
	"""
	Read TXT file to list object.
	:param string read_file_path: TXT file path.
	:return list: list object
	"""
	with open(read_file_path) as f:
		list_t = []
		lines = f.readlines()
		for line in lines:
			float_list = []
			str_t = line.replace("[", "").replace("]", "").replace("\n", "").split(",")
			for str_s in str_t:
				if str_s != "":
					float_list.append(float(str_s))
				else:
					print(read_file_path)
			list_t.append(float_list)
	
	return list_t 