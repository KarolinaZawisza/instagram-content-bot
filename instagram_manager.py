import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from envr import INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD


class InstagramManager:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTAGRAM_LOGIN)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTAGRAM_PASSWORD)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    def quit(self):
        self.driver.quit()

    def find_account(self, account_name: str):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(account_name)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
        sleep(3)

    def open_followers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(2)

    def get_followers(self):
        # followers = []
        for li in range(1, 4):
            if self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{li}]/div/div[3]/button').text == 'Follow':
                self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{li}]/div/div[3]/button').click()
        #         followers.append(self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{li}]/div/div[2]').text)
        # return followers

    @staticmethod
    def save_followers_names(followers: list):
        pass

    def close_followers(self):
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
        sleep(1)

    def like_first_post(self):
        pass
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]').click()
        # sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div/span/svg').click()
        # self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()

