from selenium import webdriver


def start_session(url):
    driver = webdriver.Firefox()
    driver.get(url)
    return driver
