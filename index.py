
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
    elif operation =='gmail':
        driver = webdriver.Firefox()
        driver.get("https://www.gmail.com")
        # assert "facebook" in driver.title
        elem = driver.find_element_by_id("identifierId")
        elem.clear()
        elem.send_keys(secrets.email)
        elem = driver.find_element_by_id("pass")
        elem.clear()
        elem.send_keys(secrets.pwd)
        elem.send_keys(Keys.RETURN)
    else:
        print('Unrecognised argument.')






if __name__ == '__main__':
    do_work()
