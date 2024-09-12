import re

data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))
