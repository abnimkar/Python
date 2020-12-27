from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/#/index')

driver.maximize_window()

driver.close()