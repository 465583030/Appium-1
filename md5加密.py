import hashlib


# def md5Encode(str):
#     m = hashlib.md5(str.encode("utf8"))
#     m.update(str)
#     return m.hexdigest()


data = "123456"
m = hashlib.md5(data.encode("utf8"))
print(m.hexdigest())