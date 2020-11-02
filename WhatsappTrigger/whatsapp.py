import html
from time import sleep

from WhatsappTrigger.WhatsappBot import WhatsappSendMsg
from bs4 import BeautifulSoup as bs
from cprint import *

class Trigger:
    def __init__(self,whatsappBot,driver):
        self.whatsapp = whatsappBot
        self.driv = driver

    def getmsg(self):
        soup = bs(self.whatsapp.gethtml(self.driv), "html.parser")
        check_list = []
        for span in soup.find_all("span", {"class": "_3Whw5 selectable-text invisible-space copyable-text"}):
            data = self.whatsapp.clean(str(span))
            clean_data = html.unescape(data)
            check_list.append(clean_data)
        return check_list[-5:]


    def send_msg(self,message):
        if message == "":
            cprint.warn("Sorry, Message cant be empty")
            return 1
        newdatatosend = message
        self.whatsapp.send_message(self.driv, newdatatosend)
        cprint.info("Checking if msg was actuallu sended")
        sleep(self.whatsapp.wait_time)
        recived_msg = self.getmsg()
        data = ""
        if newdatatosend.startswith(" "):
            data = newdatatosend[1:]
        elif newdatatosend.endswith(" "):
            data = newdatatosend[:-1]
        else:
            data = newdatatosend
        if data not in recived_msg:
            cprint.info(recived_msg[-1:][0])
            cprint.info(newdatatosend)
            while True:
                check_successor = self.TakeNoRisk(data)
                cprint.info(check_successor)
                if check_successor:
                    cprint.ok(message)
                    break
                else:
                    pass
        else:
            cprint.ok(f"message sended")

    def TakeNoRisk(self,newdatatosend):
        self.whatsapp.send_message(self.driv, newdatatosend)
        cprint.info("Checking if msg was actuallu sended")
        sleep(self.whatsapp.wait_time)
        recived_msg = self.getmsg()
        if newdatatosend in recived_msg:
            return True
        else:
            return False

