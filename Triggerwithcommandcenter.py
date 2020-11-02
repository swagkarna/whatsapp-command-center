from WhatsappTrigger import whatsapp,WhatsappBot #  import all required modules ( main modules )
from whatsappCommandExcutor.CommandExcutor import WpReciverCommand # this module will reciver msg aka command from whatsapp { main modules }
from whatsappCommandExcutor.hook import CommandHook # this modules this hook whatsapp msg with a funcation
from cprint import * # ( this modules is only for printing color full debug information )
from os import getcwd # getcwd funcation return current dir 
import threading
from time import sleep # this modules will used to wait the program


def Startcommandreciver(driv):
    reciver  = WpReciverCommand()
    setHook = CommandHook()
    while True:
        setHook.Hook(reciver.getmsg(driv))
        sleep(1)

def FireUpthreads(driv):
    reciverThread = threading.Thread(target=Startcommandreciver,args=(driv,))
    reciverThread.setDaemon(True) # set this thread in demon mode to this thread will exit with main
    reciverThread.setName("reciverThread")
    reciverThread.start() # starting the thread

try:
    app = WhatsappBot.WhatsappSendMsg(getcwd() + "/webdriver/chromedriver") # create object of sendmsg class this class will help setup everything you need to do to send msg on whatsapp this class required chromedriver path
    driv = app.find_user("tesing") # this find_user funcation will find the user and enter in his chat and will return  a chrome driver
    wapp = whatsapp.Trigger(app, driv) # this Trigger object is responsable for sending msg using WhatsappSendMsg object and the driver thats find user returned
    FireUpthreads(driv) # this funcation will fireup threader this will responsable for reciving msg in parallel
    while True:
        wapp.send_msg(input("#Enter your message => ")) # send msg funcation will send the message
        cprint.info("DONE") # print success message
except KeyboardInterrupt:
    app.quit(driv) # quit the app if user press ( ctrl + c )
    print("")
    cprint.info("Goodbye")
