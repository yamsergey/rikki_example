from allure_behave.hooks import allure_report
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from behave.model import Scenario
from rikki.appium.android import AndroidUiAutomator2Utils
from rikki.behave.context import Context


def before_all(ctx: Context):
    setattr(ctx, "appium", AppiumService())
    ctx.appium.start()
    setattr(ctx, "proxy", ctx.config.proxy)


def after_all(ctx: Context):
    ctx.proxy.shutdown()
    ctx.appium.stop()


def before_scenario(ctx: Context, scenario: Scenario):
    # start browser
    ctx.proxy.reset()
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Pixel_API_28",
        "automationName": "UiAutomator2",
        "appPackage": "com.example.car.warehouse",
        "appActivity": "com.example.car.warehouse.ui.CarsList",
        "noReset": "noReset" in scenario.tags,
        "app": "warehouse.apk",
        "forceEspressoRebuild": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    ctx.browser = driver
    setattr(ctx, "appium_utils", AndroidUiAutomator2Utils(ctx.browser))

    ctx.browser.implicitly_wait(10)


def after_scenario(ctx: Context, scenario: Scenario):
    ctx.browser.quit()
    ctx.proxy.reset()


allure_report("./reports")
