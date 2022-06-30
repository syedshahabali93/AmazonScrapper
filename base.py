import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import *
from constants import *
import math


def launch_browser():
    print("Launching Browser")
    global driver, wait1

    chromedriver_path = "/home/shahab/PycharmProjects/AmazonScrapper/chromedriver"
    driver = webdriver.Chrome(chromedriver_path)

    wait1 = WebDriverWait(driver, 10)
    driver.maximize_window()


def load_url(loading_url):
    driver.get(loading_url)

def wait_and_enter_text(ele, text):
    print(text)
    wait1.until(EC.visibility_of_element_located(ele)).send_keys(text)

def wait_and_click(element_name, ele):
    print("Clicking on: " + element_name)
    wait1.until(EC.visibility_of_element_located(ele)).click()

def wait_and_find_element(ele):
    return wait1.until(EC.visibility_of_element_located(ele))

def close_browser():
    if(browser_already_open()):
        driver.quit()

def browser_already_open():
    try:
        global driver
        if(len(driver.window_handles) == 1):
            return True
        else:
            return False
    except Exception as e:
        return False

def get_element_text(ele):
    return wait1.until(EC.visibility_of_element_located(ele)).text

def wait_for_element_and_press_enter(ele):
    wait1.until(EC.visibility_of_element_located(ele)).send_keys(Keys.ENTER)

def press_escape_button():
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def press_back_button():
    driver.execute_script("window.history.go(-1)")
