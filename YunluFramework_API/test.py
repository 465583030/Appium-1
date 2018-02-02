# Author:Xiaojingyuan
import leancloud

leancloud.init("3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz", "qXj3uIf46jB6zlcA1C4IrHSs")
msg = leancloud.Message.find_by_client("dev_e4acea4d-e6c7-4b93-b09e-1079bf6f861d")
print(msg)