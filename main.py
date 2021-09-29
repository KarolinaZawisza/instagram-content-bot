from selenium_connection import SeleniumConnection
from instagram_manager import InstagramManager

similar_accounts = []

driver = SeleniumConnection.driver
SeleniumConnection.connect_to_instagram(driver)

instagram = InstagramManager(driver)

for account in similar_accounts:
    InstagramManager.find_account(instagram, account)
    InstagramManager.follow_everyone(instagram)