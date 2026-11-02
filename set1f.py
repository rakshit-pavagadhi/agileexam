from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
LOGIN_URL = "https://the-internet.herokuapp.com/login"
SUCCESS_URL_PART = "/secure"
INVALID_CREDENTIALS_MESSAGE = "Your username is invalid!"
def login(driver, username, password):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
        username
    )
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
        password
    )
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()
def verify_successful_login(driver):
    driver.get(LOGIN_URL)
    login(driver, "tomsmith", "SuperSecretPassword!")
    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.url_contains(SUCCESS_URL_PART)), (
        "Successful login did not redirect to the dashboard"
    )
    print("Successful login verified")
def verify_invalid_login(driver):
    driver.get(LOGIN_URL)
    login(driver, "invalid_username", "invalid_password")
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert INVALID_CREDENTIALS_MESSAGE in error.text, (
        f"Unexpected error message: {error.text!r}"
    )
    print("Invalid credentials message verified")
def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        verify_successful_login(driver)
        verify_invalid_login(driver)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()
#write a dockerfile for a python based library management application, build image, run container with suitable port mapping and verify its status using docker commands
#create a git repository for a library management system, create a branch named feature/book-search, modify a python file, commit the changes, merge branch into main, display commit history
