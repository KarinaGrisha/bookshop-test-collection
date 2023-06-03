from selenium import webdriver
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
shop_btn = driver.find_element_by_css_selector('.main-nav li:nth-child(1)')
shop_btn.click()
driver.execute_script("window.scrollBy(0,400);")
book = driver.find_element_by_css_selector('.products.masonry-done li:nth-child(3)')
book.click()
header = driver.find_element_by_css_selector('.product_title.entry-title')
header_get_text = header.text
assert header_get_text == "HTML5 Forms"
driver.quit()

import time
from selenium import webdriver
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
shop_btn = driver.find_element_by_css_selector('.main-nav li:nth-child(1)')
shop_btn.click()
html_section = driver.find_element_by_css_selector('.product-categories li:nth-child(2) > a')
html_section.click()
items = len(driver.find_elements_by_class_name('attachment-shop_catalog'))
if items == 3:
    driver.execute_script("alert('There are three items in HTML category.')")
else:
    print (items)
time.sleep(4)
ok = driver.switch_to.alert
ok.accept()
driver.quit()

from selenium import webdriver
from selenium.webdriver.support.select import Select
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
shop_btn = driver.find_element_by_css_selector('.main-nav li:nth-child(1)')
shop_btn.click()
driver.execute_script("window.scrollBy(0,300);")
sorting = driver.find_element_by_css_selector('.orderby > option')
selected_value = sorting.get_attribute('value')
if selected_value == "menu_order":
    print('Default value is set')
else:
    print('any other value is set')
descending_sorting = driver.find_element_by_class_name('orderby')
select = Select(descending_sorting)
select.select_by_value('price-desc')
sorting1 = driver.find_element_by_css_selector('.orderby option:nth-child(6)')
selected_value = sorting1.get_attribute('value')
if selected_value == "price-desc":
    print('Items are sorted by price from high to low!')
else:
    print('Items are sorted in other way')
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
shop_btn = driver.find_element_by_css_selector('.main-nav li:nth-child(1)')
shop_btn.click()
driver.execute_script("window.scrollBy(0,450);")
android_book = driver.find_element_by_css_selector('.products.masonry-done li:nth-child(1)')
android_book.click()
old_price = driver.find_element_by_css_selector('.price > del > span')
old_price_value = old_price.text
assert old_price_value == "₹600.00"
new_price = driver.find_element_by_css_selector('.price ins > span')
new_price_value = new_price.text
assert new_price_value == "₹450.00"
book_preview = WebDriverWait(driver, 7).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@title,'Android')]")))
book_preview.click()
close_preview = WebDriverWait(driver, 7).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,".pp_close")))
close_preview.click()
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get('https://practice.automationtesting.in/')
shop_btn = driver.find_element_by_css_selector('.main-nav li:nth-child(1)')
shop_btn.click()
driver.execute_script("window.scrollBy(0,450);")
needed_book = driver.find_element_by_css_selector('.products.masonry-done li:nth-child(6)')
needed_book.click()
add_btn = driver.find_element_by_class_name('single_add_to_cart_button')
add_btn.click()
items_in_cart = driver.find_element_by_class_name('cartcontents')
items_in_cart_text = items_in_cart.text
assert items_in_cart_text == "1 Item"
price = driver.find_element_by_class_name('amount')
price_text = price.text
assert price_text == "₹350.00"
cart_view = driver.find_element_by_css_selector('.button.wc-forward')
cart_view.click()
subtotal = WebDriverWait(driver, 7).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), '₹350.00'))
total = WebDriverWait(driver, 7).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), '₹357.00'))
driver.quit()
