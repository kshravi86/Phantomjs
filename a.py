from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://www.eventshigh.com")
#river.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_class("home-cat-name-mob").click()
print(driver.current_url)
driver.quit()
