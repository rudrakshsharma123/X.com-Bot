from appium import webdriver
from time import sleep

def setup_appium():
    desired_caps = {
        "platformName": "Android",                  # or 'iOS' for Apple devices
        "deviceName": "emulator-5554",             # Change to your device/emulator name
        "appPackage": "com.twitter.android",       # Twitter app package name
        "appActivity": "com.twitter.app.main.MainActivity",  # Twitter main activity
        "noReset": True,                           # Prevent resetting app data
        "automationName": "UiAutomator2"           # Required for Android
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver



def post_tweet(driver, tweet_content):
    # Click the "Tweet" button
    tweet_button = driver.find_element_by_accessibility_id("Tweet")
    tweet_button.click()
    sleep(2)
    
    # Enter the tweet content
    tweet_input = driver.find_element_by_id("com.twitter.android:id/tweet_text")
    tweet_input.send_keys(tweet_content)
    sleep(2)
    
    # Send the tweet
    send_button = driver.find_element_by_accessibility_id("Send Tweet")
    send_button.click()
    sleep(3)
    
    
    
def like_post(driver):
    # Find and click the "like" button for the first post
    like_button = driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Like']")
    like_button.click()
    sleep(2)
    
    
    
def comment_on_post(driver, comment_text):
    # Open the first post
    post = driver.find_element_by_xpath("//android.widget.TextView[contains(@text, 'Reply')]")
    post.click()
    sleep(2)
    
    # Enter a comment
    comment_input = driver.find_element_by_id("com.twitter.android:id/tweet_text")
    comment_input.send_keys(comment_text)
    sleep(2)
    
    # Send the comment
    send_button = driver.find_element_by_accessibility_id("Reply")
    send_button.click()
    sleep(3)

    
def send_dm(driver, username, message_content):
    # Click on the Messages tab
    messages_tab = driver.find_element_by_accessibility_id("Messages")
    messages_tab.click()
    sleep(2)
    
    # Start a new message
    new_message_button = driver.find_element_by_accessibility_id("New Message")
    new_message_button.click()
    sleep(2)
    
    # Search for the username
    search_input = driver.find_element_by_id("com.twitter.android:id/username_or_email")
    search_input.send_keys(username)
    sleep(2)
    
    # Select the user
    user_result = driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '{}')]".format(username))
    user_result.click()
    sleep(2)
    
    # Enter the message content
    message_input = driver.find_element_by_id("com.twitter.android:id/message_input")
    message_input.send_keys(message_content)
    sleep(2)
    
    # Send the message
    send_button = driver.find_element_by_accessibility_id("Send Message")
    send_button.click()
    sleep(3)




def share_post(driver):
    # Click the "Share" button on a post
    share_button = driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Share']")
    share_button.click()
    sleep(2)
    
    # Select "Retweet" or "Quote Tweet"
    retweet_option = driver.find_element_by_xpath("//android.widget.TextView[@text='Retweet']")
    retweet_option.click()
    sleep(2)


