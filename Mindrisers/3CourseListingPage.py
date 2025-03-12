from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
    
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.mindrisers.com.np/")
driver.maximize_window()
driver.find_element(*(By.XPATH,"//a[contains(text(),'our courses')]")).click()
time.sleep(1)
link_element = driver.find_element(By.XPATH, "//a[@href='/courses/mern-stack-development-training-in-nepal']//img[@class='mb-5']")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView();", link_element)
time.sleep(1)
link_element.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)
driver.quit()
print("Test Passed")