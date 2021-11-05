from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FacebookCrawler:
    LOGIN_URL = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'
    FRIENDS_URL = 'https://www.facebook.com/friends/list'
    
    def __init__(self, login, password):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        #self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome(executable_path='C:/path/chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

        self.login(login, password)

    def login(self, login, password):
        self.driver.get(self.LOGIN_URL)
      
         

        # wait for the login page to load
        time.sleep(5)
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()
        time.sleep(10)
        self.driver.get(self.FRIENDS_URL)
        time.sleep(10)
        # wait for the main page to load
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#findFriendsNav")))

    def _get_friends_list(self):
        return self.driver.find_elements_by_css_selector(".friendBrowserNameTitle > a")

    def get_friends(self):
        # navigate to "friends" page
        self.driver.find_element_by_css_selector("a#findFriendsNav").click()

        # continuous scroll until no more new friends loaded
        num_of_loaded_friends = len(self._get_friends_list())
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: len(self._get_friends_list()) > num_of_loaded_friends)
                num_of_loaded_friends = len(self._get_friends_list())
            except TimeoutException:
                break  # no more friends loaded

        return [friend.text for friend in self._get_friends_list()]


if __name__ == '__main__':
    crawler = FacebookCrawler(login='sisesta mail', password='pas')

    for friend in crawler.get_friends():
        print(friend)