import pandas as pd

file = open("test.txt","a")

site_url = pd.read_excel("Links.xlsx")
site_url = pd.DataFrame(site_url)
List = list(site_url["URL"])


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_path = r"C:\Path_of_driver\chromedriver.exe" #Enter the path of the chrome driver here
brave_path = r"C:\Path_of_Browser\brave.exe"# Enter the path of browser here.

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

for i in range(0,len(List)):
    browser.get(List[i])
    wait = WebDriverWait(browser,600)

    title = '"entry-title"'
    x_arg = '//h1[contains(@class, '+title+')]'
    target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
    file.write(target.text)
    file.write('\n')

    title = '"td-post-content"'
    x_arg = '//div[contains(@class, ' + title + ')]'
    target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
    file.write(target.text)
    file.write('\n\n\n')