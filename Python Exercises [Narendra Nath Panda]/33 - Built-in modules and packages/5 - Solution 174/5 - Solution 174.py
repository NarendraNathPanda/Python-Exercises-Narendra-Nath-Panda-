import re

string = 'mr.NNPSB&$1423'
result = re.findall(pattern=r"\w", string=string)
print(result)