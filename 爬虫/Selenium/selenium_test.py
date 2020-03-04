from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://www.weibo.com/')
time.sleep(5)
browser.find_element_by_xpath('//div[@class="W_login_form"]/div[@class="info_list username"]//input[@id="loginname"]').send_keys('18873320898')
browser.find_element_by_xpath('//div[@class="W_login_form"]/div[@class="info_list password"]//input[@name="password"]').send_keys('6222580')
browser.find_element_by_xpath('//div[@class="W_login_form"]/div[@class="info_list login_btn"]/a[@node-type="submitBtn"]').click()



