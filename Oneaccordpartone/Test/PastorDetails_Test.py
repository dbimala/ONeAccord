

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest

from Pages1.Pastor_Details import PastorDetails


    
    
    
def pastor_details_test():
        print("Pastor Details Test Started")
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        print("Driver initialized and window maximized")
        pastor_details = PastorDetails(driver)
        pastor_details.open_page("https://payment.staging.oneaccord.cc/the-one-plan/update/30ca9f5c-2e50-4c11-9c05-e3bb4133e0a5?step=team-details")  
        time.sleep(2)
        pastor_details.yesPastor_button()
        time.sleep(1)

        pastor_details.enter_pastor_fname("John")
        time.sleep(1)

        pastor_details.enter_pastor_lname("Doe")
        time.sleep(1)

        pastor_details.enter_pastor_email("bimala.rai@oneaccord.cc")
        time.sleep(1)

        pastor_details.enter_pastor_phone("(312) 756-3418")
        time.sleep(1)

        pastor_details.click_yes_button()   
        time.sleep(2)
    
        pastor_details.click_terms_checkbox()
        time.sleep(1)
  
        pastor_details.click_next_button()
        time.sleep(2)
