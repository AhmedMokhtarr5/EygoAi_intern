from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Open the web application
driver.get("https://www.freetodolist.com/lists/new")
driver.maximize_window()
time.sleep(2)

#  Fill in list name and create
todo_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[1]/input")
todo_input.send_keys("apply for EyeGo internship" + Keys.ENTER)
time.sleep(2)
button = driver.find_element(By.XPATH,'//*[@id="item_body"]')
button.click()


# Create add task
task_input = driver.find_element(By.XPATH, '//*[@id="item_body"]')
task_input.send_keys("task 1 " + Keys.ENTER)
time.sleep(2)
button2 = driver.find_element(By.XPATH,'//*[@id="new_item"]/form/div/div[1]/input[2]')
button2.click()
print("Created task")


# mark it as completed
time.sleep(2)
checkbox = driver.find_element(By.XPATH, '//*[@id="item_complete"]')
checkbox.click()
print(" Marked as completed")

#  Delete the item
time.sleep(2)
delete_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[5]/div[1]/div/div[2]/div[2]/a')
delete_button.click()
print("Deleted the item")

#  Close browser
time.sleep(2)
driver.quit()
print(" Test completed and browser closed.")
