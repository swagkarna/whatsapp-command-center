from WhatsappTrigger import whatsapp,WhatsappBot #  import all required modules ( main modules )
from cprint import * # ( this modules is only for printing color full debug information )
from os import getcwd # getcwd funcation return current dir 

try:
    app = WhatsappBot.WhatsappSendMsg(getcwd() + "/webdriver/chromedriver") # create object of sendmsg class this class will help setup everything you need to do to send msg on whatsapp this class required chromedriver path
    driv = app.find_user("tesing") # this find_user funcation will find the user and enter in his chat and will return  a chrome driver
    wapp = whatsapp.Trigger(app, driv) # this Trigger object is responsable for sending msg using WhatsappSendMsg object and the driver thats find user returned
    while True:
        wapp.send_msg(input("#Enter your message => ")) # send msg funcation will send the message
        cprint.info("DONE") # print success message
except KeyboardInterrupt:
    app.quit(driv) # quit the app if user press ( ctrl + c )
    print("")
    cprint.info("Goodbye")
