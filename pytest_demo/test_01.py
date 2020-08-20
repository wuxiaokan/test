from selenium import webdriver
import time


# ** 作者：上海-悠悠 QQ交流群：588402570**

def test_yoyo_01(browser):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert t == "上海-悠悠"



