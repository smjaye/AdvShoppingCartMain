import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'***************************************************************')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to advantage shopping cart website
    driver.get(locators.advantage_shopping_url)

    # check that  URL and the home page title are as expected
    if  driver.current_url == locators.advantage_shopping_url and locators.advantage_shopping_homepage_title in driver.title :
        print(f'*************Validating title and URL***********************************************')
        print(f'Hurrey! {locators.app} App website launched successfully!')
        print(f' Current URL : {driver.current_url}')
        print(f' Homepage title: {driver.title}')
        sleep(4)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL : {driver.current_url}')
        print(f' HomePage title: {driver.title}')
        tearDown()



def tearDown():
    if driver is not None:
        print(f'******************************************************')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def sign_up():
    print(f'***************************************************************************')
    if driver.current_url == locators.advantage_shopping_url: # check we are on home page
        driver.find_element(By.ID, 'menuUserSVGPath').click()
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(0.25)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
        sleep(0.25)
        driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
        ##########################################################################################
        # PRESS REGISTER BUTTON TO COMPLETE REGISTRATION
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.25)
        print(f' New user account is created')
        ################################################################################


def check_full_name():
    print(f'*******************************************************************************')
    if driver.current_url == locators.advantage_shopping_url:  # check we are on home page
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
        sleep(0.5)
        print(f'************Validating Full name is displayed*********************************')
        if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
            print(f'You are in your account page: {locators.full_name}.')
        else:
            print(f'Something is not right, account page is not displayed')



def check_orders():
    print(f'********************************************************************')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(0.5)
    print(f'****************Validating to check there is - No Orders********************')
    if driver.current_url == locators.advantage_shopping_orderpage_url:
        driver.find_element(By.XPATH, '//label[contains(., " - No orders - ")]').is_displayed()
        print(f'Sorry!You have no orders')
    else:
        print(f'Something is not right')


def log_out():
    print(f'**********************************************************************')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    sleep(0.25)
    print(f'You have successfully logged out, feel free to log in again!')


def log_in():
    print(f'***********************************************')
    print(f'Hello! You are Welcome in your homepage again. Feel free to log in and shop')
    if driver.current_url == locators.advantage_shopping_url: # check we are on home page
        print(driver.current_url)
        driver.find_element(By.ID, 'menuUserSVGPath').click()
        sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.25)
        print(f'The username is displayed: {locators.username}')
        print(f'So, Hai! You have logged in again')


def delete_test_account():
    print(f'***************Delete the Account***************************')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(3)

    print(f'***********************Verify account is deleted*************************')

    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(1)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)

    if driver.find_element(By.ID, 'signInResultMessage').is_displayed():
        print(f'-------Incorrect user name or password message is displayed.')
        print(f'--------You have deleted the account of {locators.username}----')
        print(f'*************This test is passed at: {datetime.datetime.now()}*************')
    else:
        print('There is something wrong')








# setUp()
# sign_up()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# tearDown()

