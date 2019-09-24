# noinspection PyUnresolvedReferences
import rikki.behave.steps.proxy
from behave import *
from rikki.appium.common import AppiumUtils
from rikki.appium.common import Direction, SwipeSpeed
from rikki.behave.context import Context
from selenium.webdriver.common.by import By
import time


@given("Scroll like a monkey")
def step_scroll(context: Context):
    context.appium_utils.swipe(direction=Direction.DOWN, speed=SwipeSpeed.FAST)
    context.appium_utils.swipe(direction=Direction.DOWN, speed=SwipeSpeed.MEDIUM)
    context.appium_utils.swipe(direction=Direction.UP, speed=SwipeSpeed.SLOW)
    context.appium_utils.swipe(direction=Direction.UP, speed=SwipeSpeed.SLOW)


@given("Wait for cars list loaded")
def step_wait_for_list(context):
    utils: AppiumUtils = context.appium_utils
    utils.wait(by=By.ID, locator="carItemIdText")


@given("relaunch")
def step_impl(context: Context):
    context.proxy.clean_up()
    context.appium_utils.relaunch_app()


@given("Wait forever")
def step_impl(context):
    while True:
        time.sleep(360)
