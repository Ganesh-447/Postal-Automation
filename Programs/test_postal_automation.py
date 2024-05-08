import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


def test_postal_login():
    driver = webdriver.Chrome()
    driver.get("https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y")
    driver.maximize_window()
    time.sleep(20)
    agent_id = driver.find_element(By.XPATH, "//input[@name ='AuthenticationFG.USER_PRINCIPAL']")
    password = driver.find_element(By.XPATH, "//input[@name ='AuthenticationFG.ACCESS_CODE']")
    log_in = driver.find_element(By.XPATH, "//input[@value ='Log in']")
    agent_id.send_keys("")
    password.send_keys("")
    log_in.click()
    time.sleep(20)
    accounts = driver.find_element(By.XPATH, "//a[@id='Accounts']")
    accounts.click()
    time.sleep(10)
    books_screen = driver.find_element(By.XPATH, "//a[@id='Agent Enquire & Update Screen']")
    books_screen.click()
    time.sleep(10)
    cash = driver.find_element(By.XPATH,"//input[@id = 'CustomAgentRDAccountFG.PAY_MODE_SELECTED_FOR_TRN' and @value ='C']")
    cash.click()
    account_id = driver.find_element(By.NAME, "CustomAgentRDAccountFG.ACCOUNT_NUMBER_FOR_SEARCH")
    account_id.send_keys()
    fetch = driver.find_element(By.XPATH,"//input[@name='Action.FETCH_INPUT_ACCOUNT']")
    fetch.click()
    time.sleep(5)
    select_book = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for checkbox in select_book:
        checkbox.click()
    save = driver.find_element(By.XPATH,"//input[@name='Action.SAVE_ACCOUNTS']")
    save.click()
    time.sleep(4 * 60 * 60)  # 4 hours,020011116491



