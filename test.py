from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, json

with open("browsers.json", "r") as f:
    obj = json.loads(f.read())

driver = webdriver.Remote(
  desired_capabilities=caps)

driver.get("http://www.google.com")
inputElement = driver.find_element_by_name("q")
inputElement.send_keys("browserstack")
inputElement.submit()
print driver.title
driver.quit()
