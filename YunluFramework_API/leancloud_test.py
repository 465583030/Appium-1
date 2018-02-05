# Author:Xiaojingyuan

import leancloud
# conversation = leancloud.Conversation.query.first()


leancloud.init("3BXiD9Fga5RtswdyrJSFQ3h3-gzGzoHsz", "qXj3uIf46jB6zlcA1C4IrHSs")
messages = leancloud.Message.find_by_client('a8d08367-7959-477d-9887-1cf3db8f9fb0')