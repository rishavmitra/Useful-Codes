from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\risha\PycharmProjects\pythonNPTEL\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://web.whatsapp.com/")

wait = WebDriverWait(browser,600)
target ='"Golu"'
string = "This is an automated message sent using python"
x_arg = '//span[contains(@title, '+ target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name('p3_M1')
for i in range(100):
    input_box.send_keys(string+Keys.ENTER)