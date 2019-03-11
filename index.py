
import sys
import secrets
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def do_work():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for a in args:
            if a == '--help':
                print('Basic command line program')
                print('Options:')
                print('    --help -> show this basic help menu.')
                print('    --facebook -> facebook.')
                print('    --veg -> show a random vegetable')
            elif a == '--facebook':
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
                # driver.close()
            elif a == '--veg':
                print(random.choice(['Carrot', 'Potato', 'Turnip']))
            else:
                print('Unrecognised argument.')

if __name__ == '__main__':
    do_work()
