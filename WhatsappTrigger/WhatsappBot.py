from os import system, getcwd
from time import sleep

from WhatsappTrigger import banner
from cprint import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WhatsappSendMsg:
    def __init__(self,driver_path):
        self.wait_time = 1
        self.driverpath = driver_path

    def clean(self,data):
            return data.replace('<span class="_3Whw5 selectable-text invisible-space copyable-text" dir="ltr"><span>',"").replace('</span></span>',"").replace('<span class="_3Whw5 selectable-text invisible-space copyable-text" dir="auto"><span>',"")

    def gethtml(self,driver):
        sleep(self.wait_time)
        htmlpage = driver.page_source
        return htmlpage

    def send_message(self,driver,message):
        sleep(self.wait_time)
        driver.find_element_by_class_name("_3uMse").send_keys(message + Keys.ENTER)
    
    def quit(self,driver):
        driver.quit()


    def search_groudn(self,driver,GroupName):
        driver.find_element_by_class_name("_3FRCZ").send_keys(GroupName)
        cprint.info("searching tesing group ")
        sleep(self.wait_time)
        driver.find_element_by_class_name("_2kHpK").click()
        cprint.info("click of the first person of the list")
        sleep(self.wait_time)
        return driver

    def find_user(self,GroupName):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        #options.add_argument("headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        try:
            driver = webdriver.Chrome(executable_path=self.driverpath, options=options)
            system("clear")
            cprint.warn(banner.PrintBanner())
            cprint.info("Press Enter when you login into web.whatsapp")
        except Exception as e:
            cprint.err(str(e))

        driver.get("https://web.whatsapp.com/")
        driver.set_window_size(1365, 716)
        input()
        driver.find_element_by_class_name("_3FRCZ").click()
        cprint.info("search bar click successfull")
        driverx = self.search_groudn(driver,GroupName)
        return driverx