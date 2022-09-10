from selenium import webdriver
from selenium.webdriver.common.by import By

# Environment Variables
USER = 'Your username here'
PASS = 'Your password here'

# Chrome Web Driver - Incognito Mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# driver.minimize_window() works but can't scrape
driver.get('https://www.bankofamerica.com')


# Login Page
UsernamePath = "//input[@id='onlineId1']"
PasswordPath = "//input[@id='passcode1']"
LoginButtonPath = "//button[@id='signIn']"
AuthSelectedMethodPath = "//label[text()='Text message']"
SendCodeButtonPath = "//span[text()='SEND CODE']"


# LOGIN PAGE ___________________________________________________________________

# Enter username
try:
    UserElement = driver.find_elements(By.XPATH, UsernamePath)[0]
    UserElement.send_keys(USER)
    print('Success: Login username entered')
except:
    print('Fail: Login username entered')


# Enter password
try:
    PasswordElement = driver.find_elements(By.XPATH, PasswordPath)[0]
    PasswordElement.send_keys(PASS)
    print('Success: Login password entered')
except:
    print('Fail: Login password entered')


# Click sign in
try:
    LoginButtonElement = driver.find_elements(By.XPATH, LoginButtonPath)[0]
    LoginButtonElement.click()
    print('Success: Login button clicked')
except:
    print('Fail: Login button clicked')



# Implicityly Waiting for screen to change _______________________________________
driver.implicitly_wait(30)
print('Waiting for screen change ~30 sec ...')


# Click How would you like to receive the Authorization Code
try:
    AuthSelectMethod = driver.find_elements(
        By.XPATH, AuthSelectedMethodPath)[0]
    AuthSelectMethod.click()
    print('Success: Auth method selected')
except:
    print('Fail: Auth method selected')



# Click Send Code
try:
    SendCodeButtonElement = driver.find_elements(
        By.XPATH, SendCodeButtonPath)[0]
    SendCodeButtonElement.click()
    print('Success: Send Code button clicked')
except:
    print('Fail: Send Code button clicked')


# driver.quit()
