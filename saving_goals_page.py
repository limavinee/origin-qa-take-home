from selenium import webdriver
from selenium.webdriver.common.by import By

class SavingGoalsPage:
    driver = webdriver.Chrome()
    money_input_locator = driver.find_element(By.XPATH,"//input['1,000']")
    #date_input_locator =
    #date_input_left_button_locator =
    #date_input_right_button_locator =
    #monthly_amount_locator =
    #confirm_button_locator = //button[.='Confirm']
