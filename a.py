from selenium import webdriver
driver = webdriver.Chrome()
driver.set_window_size(1120, 550)
driver.get("https://www.eventshigh.com")
driver.find_element_by_name('events').send_keys("realpython")
#river.find_element_by_class_name("home-cat-name-mob").click()
print(driver.current_url)
driver.quit()
