try:
  import unzip_requirements
except ImportError:
  pass

import json


def webhook(event, context):
    import numpy as np
    return {
        "status":200,
        "msg": "success"
    }

