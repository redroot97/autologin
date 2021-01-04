from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 50)

url="LOGIN URL"
username = '********'
password = '********'
driver.get (url)
wait.until(EC.url_contains('login_challenge'))
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_tag_name("button").click()
driver.implicitly_wait(20)

elem1= driver.find_element_by_xpath("//ul[@class='nav nav-tabs parent']")
elem1.find_element_by_xpath(".//a[@href='#home-dashboard-3']").click()
driver.implicitly_wait(10)

elem2= driver.find_element_by_xpath("//div[@class='markAttendancePanel']")
elem2.find_element_by_xpath(".//button[@class='btn btn-large btn-success signIn']").click()
