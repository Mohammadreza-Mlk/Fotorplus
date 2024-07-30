from _ast import expr
import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
from watchlog import Watchlog
watchlog_instance = Watchlog()

watchlog_instance.increment('Account_Created')

time.sleep(10)

watchlog_instance.increment('Account_AddTo_PlusMesenger')