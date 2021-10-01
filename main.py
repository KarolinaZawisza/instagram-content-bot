from selenium_connection import SeleniumConnection
from instagram_manager import InstagramManager

target_accounts = ['tahliastanton', 'lovejoyonline', 'alecbenjamin']
# target_accounts = ['karljacobs']

driver = SeleniumConnection.driver
SeleniumConnection.connect_to_instagram(driver)

instagram = InstagramManager(driver)
instagram.log_in()

try:
    for account in target_accounts:
        instagram.find_account(account)
        instagram.open_followers()
        followers = instagram.get_followers()
        # instagram.save_followers_names(followers)
        instagram.close_followers()
        # instagram.like_first_post()

except Exception as exception:
    print(f'{exception}')
    instagram.quit()

instagram.quit()
