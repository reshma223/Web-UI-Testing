#Home Page Load- Ensure the website loads correctly with no errors.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run in headless mode (no UI, optional)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Step 1: Open the website
    url = "https://www.google.com/"
    driver.get(url)
    time.sleep(5)
    drop_down_field=driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Mindrisers")
    # select=select(drop_down_field)
    # select.select_by_index(0)
    # time.sleep(5)

#     # Step 2: Check if the page loads correctly
#     print("Page Title:", driver.title)
#     assert "Mindrisers" in driver.title, "Home Page Title is incorrect!"

#     # Step 3: Check if key elements exist (Example: Logo, Header, Footer)
#     assert driver.find_element(By.TAG_NAME, "body"), "Page body not found!"
#     assert driver.find_element(By.TAG_NAME, "header"), "Header not found!"
#     assert driver.find_element(By.TAG_NAME, "footer"), "Footer not found!"

#     # Step 4: Check if there are no error messages
#     page_source = driver.page_source.lower()
#     error_keywords = ["404", "error", "not found", "server error"]
    
#     for keyword in error_keywords:
#         assert keyword not in page_source, f"Error detected on page: {keyword}"

#     print("✅ Home Page Loaded Successfully!")

# except Exception as e:
#     print(f"❌ Test Failed: {e}")

finally:
    driver.quit()

