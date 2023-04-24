import re

raw_text = "Send an email to mr.narendranathpanda@gmail.com or narendranathpanda1423@gmail.com"
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)