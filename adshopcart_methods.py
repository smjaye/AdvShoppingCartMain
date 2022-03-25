import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'__________________________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to advantage shopping cart website
    driver.get(locators.advantage_shopping_url)

    # check that  URL and the home page title are as expected
    if  driver.current_url == locators.advantage_shopping_url and locators.advantage_shopping_homepage_title in driver.title:
        print(f'-----Validating title and URL----------------------------------------------------')
        print(f'Hurrey! {locators.app} App website launched successfully!')
        print(f' Current URL : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        sleep(0.5)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL : {driver.current_url}')
        print(f' HomePage title: {driver.title}')
        tearDown()



def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
tearDown()