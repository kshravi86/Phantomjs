from selenium import webdriver
driver = webdriver.PhantomJS()
#driver.set_window_size(1120, 550)
driver.get("https://www.google.com")
#river.find_element_by_name('events').send_keys("realpython")
#river.find_element_by_class_name("home-cat-name-mob").click()
print(driver.current_url)
driver.quit()
