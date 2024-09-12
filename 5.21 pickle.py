import pickle

data = ...  # some Python object
f = open('somefile', 'wb')
# 存储到文件中
pickle.dump(data, f)
# 将对象存储为字符串
s = pickle.dumps(data)


# 从文件中读取
f = open('somefile', 'rb')
data = pickle.load(f)

# 从字符串中读取
data = pickle.loads(s)
