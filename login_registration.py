from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50')
account.click()
email = driver.find_element_by_id('reg_email')
email.send_keys('karina.grisha@gmail.com')
password = driver.find_element_by_id('reg_password')
password.send_keys('Rapa01_Nui55')
time.sleep (15)
password_check = WebDriverWait(driver, 25).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-password-strength"), "Strong"))
register_btn = driver.find_element_by_xpath('//input[@name="register"]')
register_btn.click()
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://practice.automationtesting.in/')
account = driver.find_element_by_id('menu-item-50')
account.click()
login = driver.find_element_by_id('username')
login.send_keys('karina.grisha@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('Rapa01_Nui55')
login_btn = driver.find_element_by_xpath('//input[@name="login"]')
login_btn.click()
logout = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout")))
print('Logout detected!')
driver.quit()



