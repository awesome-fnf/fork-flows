# -*- coding: utf-8 -*-
import json
import os
import logging
import time

def handler(event, context):
  logger = logging.getLogger()
  evt = json.loads(event)
  logger.info("Handling event: %s", evt)

  return {"value": 
    {
      "key": evt["key"],
      "time": int(time.time())
    }
  }