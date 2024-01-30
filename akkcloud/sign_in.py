import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

baseUrl = "https://akkcloud.com/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(baseUrl)

home_web = driver.find_element(By.TAG_NAME, "a")
url = home_web.get_attribute("href")

driver.get(url)

driver.find_element(By.ID, "email").send_keys(os.environ.get("email"))
driver.find_element(By.ID, "password").send_keys(os.environ.get("password"))

time.sleep(1)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "login_submit"))
).click()

signin_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="kt_subheader"]/div/div[2]/a'))
)
if signin_button.get_attribute("disabled"):
    print("已经签到过了")
else:
    signin_button.click()
    time.sleep(1000)
    if signin_button.get_attribute("disabled") != "disabled":
        print("签到失败")
    else:
        print("签到成功")

driver.close()
