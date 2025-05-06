#Contact Form Submission-	Fill in the form with valid/invalid inputs and verify success/error messages.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from faker import Faker
import  time

fake = Faker()
random_name = fake.name()
random_email = fake.user_name() + "@gmail.com"
random_phone = fake.numerify('##########')
random_address = fake.address()
random_subject = fake.sentence()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.mindrisers.com.np/")
driver.maximize_window()
time.sleep(1)
Contact_Us=driver.find_element(*(By.XPATH,"//a[normalize-space()='contact us']"))
Contact_Us.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 700);")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(random_name)
driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(random_email)
driver.find_element(By.XPATH, "//input[@placeholder='Phone']").send_keys(random_phone)
driver.find_element(By.XPATH, "//input[@placeholder='Subject']").send_keys(random_subject)
driver.find_element(By.XPATH, "//textarea[@placeholder='Queries']").send_keys(random_subject)
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
time.sleep(5)
# driver.quit()