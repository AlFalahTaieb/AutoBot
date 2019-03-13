
import sys
import secrets
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def do_work():
        
    operation = input('''
    Please type in the math operation you would like to complete:
            facebook to connect to facebook
            gmail to connect to gmail
            hattrick to connect to hattrick
            reddit to connect to reddit
    ''')

    if operation == 'facebook':
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com")
        # assert "facebook" in driver.title
        elem = driver.find_element_by_id("email")
        elem.clear()
        elem.send_keys(secrets.email)
        elem = driver.find_element_by_id("pass")
        elem.clear()
        elem.send_keys(secrets.pwd)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    elif operation =='hattrick':
        driver = webdriver.Firefox()
        driver.get("https://www.hattrick.org")
        # assert "facebook" in driver.title
        elem = driver.find_element_by_id("ctl00_CPContent_ucLogin_txtUserName")
        elem.clear()
        elem.send_keys(secrets.usernameh)
        elem = driver.find_element_by_id("ctl00_CPContent_ucLogin_txtPassword")
        elem.clear()
        elem.send_keys(secrets.pwdh)
        elem.send_keys(Keys.RETURN)
    elif operation =='reddit':
        driver = webdriver.Firefox()
        driver.get("https://old.reddit.com/")
        # assert "facebook" in driver.title
        elem = driver.find_element_by_name("user")
        elem.clear()
        elem.send_keys(secrets.usernameR)
        elem = driver.find_element_by_name("passwd")
        elem.clear()
        elem.send_keys(secrets.passR)
        elem.send_keys(Keys.RETURN)
    else:
        print('Unrecognised argument.')






if __name__ == '__main__':
    do_work()
