import requests
import json

url = "https://3bxid9fg.api.lncld.net/1.1/rtm/messages/history"

headers = {
    'X-LC-Id': "3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz",
    'X-LC-Sign': "7396816f73bdbcf70281b09dc2c1b3b9,1517046641139,master",
    'Cache-Control': "no-cache",
    'Postman-Token': "9097a14d-f18b-bdc5-304e-bebd11590d51"
    }
data = {
    "conv-id":"fe4cad7676f0879160e9db87b0bdbec6"

}
response = requests.request("GET", url, headers=headers)


print(response.text)