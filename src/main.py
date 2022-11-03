import selenium
from selenium import webdriver
driver = webdriver.Chrome()

username = '1487500@learn.vsb.bc.ca'
password = 'student'

driver.get('https://myeducation.gov.bc.ca/aspen/logon.do')
username_box = driver.find_element('name', 'username')
password_box = driver.find_element('name', 'password')
logon_button = driver.find_element('name', 'logonButton')

username_box.send_keys(username)
password_box.send_keys(password)


#logon_button.click()