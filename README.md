# whatsapp-command-center
This is a old fun project i code it on my free time

### How to use without command center
```python
from WhatsappTrigger import whatsapp,WhatsappBot
from cprint import *

try:
    app = WhatsappBot.WhatsappSendMsg()
    driv = app.find_user("tesing")
    wapp = whatsapp.Trigger(app, driv)
    while True:
        wapp.send_msg(input("#Enter your message => "))
        cprint.info("DONE")
except KeyboardInterrupt:
    app.quit(driv)
    print("")
    cprint.info("Goodbye")

```

### how to use with command center 
```python
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
```
### how to use create a connect funcation with a command
```python
1. Go inside whatsappCommandExcutor folder open hookfuncation.py and you can create your func here
example : {
    def msg(self):  # DEMO FUNCATION
        cprint.info("helow from msg funcation")
}
2. open hooklist.py and create connector 
example : {
	    def Hookslist(self):
        return {
            "@sendmsg": "msg",
            "@deletemsg": "del"
            "@add your new command here": "your funcation name here"
        }
}
```
### Requirement
* python3.8
* selenium
* cprint
