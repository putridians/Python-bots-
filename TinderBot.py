from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TinderBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot 
        bot.get('https://tinder.com/')
        time.sleep(3)
        link = bot.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        link.click()
        time.sleep(3)
        link2 = bot.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        link2.click()
        time.sleep(3)
        base_window = bot.window_handles[0]
        new_window = bot.window_handles[1]
        bot.switch_to.window(new_window)
        phone = bot.find_element_by_xpath('//*[@id="email"]')
        password = bot.find_element_by_xpath('//*[@id="pass"]')
        phone.clear() 
        password.clear() 
        phone.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.switch_to_window(base_window)
        link3 = bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        link3.click()
        time.sleep(3)
        link4 = bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        link4.click()
        
        link5 = bot.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        link5.click()
        time.sleep(3)
        link6 = bot.find_elements_by_link_text('Allow Location Access')
        link6.click()
        

    def like(self):
        bot = self.bot 

andybot = TinderBot('5036863678', 'Dragonslayer6969')
andybot.login()