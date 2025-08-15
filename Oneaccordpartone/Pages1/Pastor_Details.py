
from selenium.webdriver.common.by import By

class PastorDetails:
    def __init__(self, driver):
       self.driver = driver
       self.pastor_Fname = (By.XPATH,
             "//input[@data-testid='onboarding-pastor-first-name-input']")
       
       self.pastor_error_Fname = (By.XPATH, 
            "//div[@data-testid='onboarding-pastor-first-name-input-error-message']")
       
       self.pastor_Lname = (By.XPATH,
             "//input[@data-testid='onboarding-pastor-last-name-input']")
       
       self.pastor_error_Lname = (By.XPATH, 
            "//div[@data-testid='onboarding-pastor-last-name-input-error-message']")
       
       self.pastor_email = (By.XPATH, 
             "//input[@data-testid='onboarding-pastor-email-input']")
       
       self.pastor_email_error = (By.XPATH, 
             "//div[@data-testid='onboarding-pastor-email-input-error-message']")
       
       self.pastor_phone = (By.XPATH,
             "//input[@data-testid='onboarding-pastor-phone-input']")
       
       self.pastor_phone_requireerror = (By.XPATH, 
            "//div[@data-testid='onboarding-pastor-phone-input-error-message']")
       
       self.Yes_button = (By.XPATH, 
            "//button[@data-testid='onboarding-managed-by-pastor-yes-radio']")
       
       self.terms_checkbox = (By.XPATH,
        "//button[@data-testid='onboarding-terms-agreed-checkbox']")    
       
       self.next_button = (By.XPATH,
            "//button[@data-testid='onboarding-next-step-btn']")
       
       self.yesPastor_button=(By.XPATH,"//button[@data-testid='onboarding-assigned-pastor-yes-btn']")
       

    def open_page(self, url): 
        self.driver.get(url)
        self.driver.maximize_window()   

    def enter_pastor_fname(self, fname):
        self.driver.find_element(*self.pastor_Fname).send_keys(fname)

    def enter_pastor_lname(self, lname):
        self.driver.find_element(*self.pastor_Lname).send_keys(lname) 

    def enter_pastor_email(self, email):
        self.driver.find_element(*self.pastor_email).send_keys(email)

    def enter_pastor_phone(self, phone):
        self.driver.find_element(*self.pastor_phone).send_keys(phone)

    def click_yes_button(self):
        self.driver.find_element(*self.Yes_button).click()

    def click_terms_checkbox(self):
        self.driver.find_element(*self.terms_checkbox).click()

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click() 

    def Click_pastor_yes_button(self):
        self.driver.find_element(*self.Yes_button).click()











