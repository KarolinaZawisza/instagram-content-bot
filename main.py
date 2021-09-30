from selenium_connection import SeleniumConnection
from instagram_manager import InstagramManager

target_accounts = ['tahliastanton', 'lovejoyonline', 'alecbenjamin']

driver = SeleniumConnection.driver
SeleniumConnection.connect_to_instagram(driver)

instagram = InstagramManager(driver)
InstagramManager.log_in(instagram)

try:
    for account in target_accounts:
        InstagramManager.find_account(instagram, account)
        InstagramManager.open_followers(instagram)
        followers = InstagramManager.get_followers(instagram)
        # InstagramManager.save_followers_names(followers)
        InstagramManager.close_followers(instagram)
        InstagramManager.quit(instagram)

except Exception as exception:
    print(f'Error: {exception}')
    InstagramManager.quit(instagram)
