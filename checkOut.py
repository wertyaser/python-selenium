# selenium 4
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://unipc.com.ph/my-account/")

#unipc login
uniUser = driver.find_element(By.NAME, 'username')
uniUser.send_keys("sample@gmail.com")
uniUser.send_keys(Keys.TAB)

uniPass = driver.find_element(By.NAME, 'password')
uniPass.send_keys("samplepass")
uniPass.send_keys(Keys.RETURN)

#search item
# driver.find_element(By.NAME, 's').click()
# uniSearch = driver.send_keys("Apacer flashdrive")
# uniSearch.send_keys(Keys.RETURN)



