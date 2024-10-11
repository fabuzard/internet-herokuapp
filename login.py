from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set the path to your WebDriver
driver_path = 'D:\\webdriver\\msedgedriver.exe' 
service=Service(driver_path)
driver=webdriver.Edge(service=service)

# Open a website
driver.get('https://the-internet.herokuapp.com/login')


driver.find_element(By.ID,("username")).send_keys("tomsmith")

driver.find_element(By.ID,("password")).send_keys("SuperSecretPassword!")

driver.find_element(By.CLASS_NAME,("radius")).click()
# Print the page title
print(driver.title)

time.sleep(5) 

# Close the browser
driver.quit()
