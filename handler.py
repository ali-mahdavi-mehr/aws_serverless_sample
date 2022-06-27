#when you use serverless-python-requirement
#this library collect all dependencies to a file named .requirements.zip
#so we unzip libs
try:
  import unzip_requirements
except ImportError:
  pass

import json


#your main handle
# all request that you add in severless.yml send to this function
# in our app all GET request will send to this function
def webhook(event, context):
    import numpy as np
    return {
        "status":200,
        "msg": "success"
    }

