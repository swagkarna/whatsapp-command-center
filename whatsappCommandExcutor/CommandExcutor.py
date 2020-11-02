import html
from time import sleep

from bs4 import BeautifulSoup as bs


class WpReciverCommand:
    def __init__(self):
        self.wait_time = 1

    def clean(self, data):
        return data.replace('<span class="_3Whw5 selectable-text invisible-space copyable-text" dir="ltr"><span>',
                            "").replace('</span></span>', "").replace(
            '<span class="_3Whw5 selectable-text invisible-space copyable-text" dir="auto"><span>', "")

    def gethtml(self, driver):
        sleep(self.wait_time)
        htmlpage = driver.page_source
        return htmlpage

    def getmsg(self, driver):
        soup = bs(self.gethtml(driver), "html.parser")
        check_list = []
        for span in soup.find_all("span", {"class": "_3Whw5 selectable-text invisible-space copyable-text"}):
            data = self.clean(str(span))
            clean_data = html.unescape(data)
            check_list.append(clean_data)
        return check_list[-5:]
