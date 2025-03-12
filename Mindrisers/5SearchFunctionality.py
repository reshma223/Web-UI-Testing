from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_course(driver, search_term):
    driver.get("https://www.mindrisers.com.np/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[contains(text(),'our courses')]").click()
    time.sleep(2)

    search_box = driver.find_element(By.XPATH, "//input[@name='searchTerm']")
    driver.execute_script("arguments[0].scrollIntoView();", search_box)
    time.sleep(1)
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)

    try:
        no_results = driver.find_element(By.XPATH, "//p[contains(text(),'0 course found matching')]")
        print(f"❌ No results found for '{search_term}' - {no_results.text}")
    except:
        results = driver.find_elements(By.XPATH, "//section[1]//div[2]//div[1]//ul[1]")
        if results:
            print(f"✅ Search successful for '{search_term}'")
        else:
            print(f"⚠️ Unexpected issue occurred while searching for '{search_term}'!")

            
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
search_course(driver, "python")
search_course(driver, "InvalidKeyword123")

driver.quit()
print("Test Passed")