from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from bs4 import BeautifulSoup
from lxml import etree
import requests
  

import os

# Set up the web driver
driver = webdriver.Chrome()
url = "https://flowscan.org"
driver.get(url)

# Wait for 30 seconds before retrieving the page source
time.sleep(10)
k = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]')

div_elements = k.find_elements(By.XPATH,'./div/div')

hrefs=[]
while len(hrefs)<1000:
    for i in div_elements:
       
        try:
            a_tag = i.find_element(By.XPATH, './div/a')
            href = a_tag.get_attribute('href')
            print(href)
            hrefs.append(href)
            URL = href+'/script'
            driver1 = webdriver.Chrome()
            driver1.get(URL)
            time.sleep(5)
            k1= driver1.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/pre/code')

            # Check if codesamples folder exists or not, create it if it doesn't exist
            if not os.path.exists('codesamples'):
                os.makedirs('codesamples')
            
            # Save the text in a .txt file with the name len(hrefs) in codesamples folder
            with open(f'codesamples/{len(hrefs)}.txt', 'w', encoding='utf-8') as f:
                f.write(k1.text)
        
            driver1.quit()
        
        except Exception as e:
        # if any error occurs, log the error and continue with the next element
            continue
   
       

    
    time.sleep(10) 
    k = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]')

    div_elements = k.find_elements(By.XPATH,'./div/div')
    # Wait for new transactions to appear
    
# Close the browser window
driver.quit()
