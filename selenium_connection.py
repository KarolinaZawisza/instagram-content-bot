from selenium import webdriver


class SeleniumConnection:
    cdp = 'C:\Development\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=cdp)

    @staticmethod
    def connect_to_instagram(driver):
        driver.get('https://www.instagram.com/')
