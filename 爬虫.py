import requests

r = requests.get("https://www.yunlu6.com")
print(r.url)
print(r.text)
