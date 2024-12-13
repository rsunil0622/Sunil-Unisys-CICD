from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
# we are only import webdriver from entire selenium
 
# Setting up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU (Windows-specific)
chrome_options.add_argument("--no-sandbox")  # Required for running as root in Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
 
# Initializing the web driver with options
service = Service("/usr/bin/chromedriver")  # Update the path to chromedriver
chrome_driver = webdriver.Chrome(service=service, options=chrome_options)


# loading particular driver of browser 
# initilizing web driver 
chrome_driver = webdriver.Chrome()
# opening a web url 
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")


#selenium can find elements
#name classname id cssSelector
#chrome_driver.find_element(By.NAME,"name").send_keys("Sunil")
chrome_driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Sunil")
chrome_driver.find_element(By.NAME,"email").send_keys("Sunil@linux.com")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("HelloCloud@123")
#click the box
chrome_driver.find_element(By.ID,"exampleCheck1").click()


#dropdown
my_select = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
#we can select data by index, visible text as well
my_select.select_by_index(0)
#my_select.select_by_visible_text("Female")

#using css_selector for radio button
chrome_driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#submit
chrome_driver.find_element(By.XPATH,"//input[@type='submit']").click()

#find the message data
message = chrome_driver.find_element(By.CLASS_NAME,"alert-success").text

time.sleep(3)

print(message)
#message validation
assert "Success" in message

#print the page title
print("Page title : ",chrome_driver.title)
#current url
print("Page url : ",chrome_driver.current_url)
#saving screenshot
chrome_driver.save_screenshot('pagehome.png')
print('current page screenshot saved')
# closing my driver / stopping  
chrome_driver.quit()