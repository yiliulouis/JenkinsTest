from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Downloads\chromedriver_win32 (1)\chromedriver")
site = "www.python.org"
url = 'https://' + site
driver.get(url)
driver.implicitly_wait(10)


