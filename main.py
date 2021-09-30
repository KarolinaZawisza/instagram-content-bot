from selenium_connection import SeleniumConnection
from instagram_manager import InstagramManager

target_accounts = ['tahliastanton', 'lovejoyonline', 'alecbenjamin']
# target_accounts = ['karljacobs']

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
        # InstagramManager.like_first_post(instagram)

except Exception as exception:
    print(f'{exception}')
    InstagramManager.quit(instagram)

InstagramManager.quit(instagram)

