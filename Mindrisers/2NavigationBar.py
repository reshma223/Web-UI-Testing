from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_navigation_links():
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.mindrisers.com.np/")
    driver.maximize_window()
    
    menu_items = [
        "Our Courses",
        "Post +2 Courses",
        "Placement Partner",
        "Successful Stories",
        "Blogs",
        "Contact Us",
        "Admission"  
    ]
        
    for item in menu_items:
        try:
            link = driver.find_element(By.LINK_TEXT, item)
            link.click()
            print(f"✅ Clicked on: {item}")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.get("https://www.mindrisers.com.np/")
            time.sleep(2)  
        except Exception as e:
            print(f"❌ Failed to click on {item}: {e}")
# Run the test
test_navigation_links()
