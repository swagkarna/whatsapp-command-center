# this find will excute the funcation according tot he hooklist hooks

from cprint import *
from whatsappCommandExcutor.hookfuncation import HookFunc
from whatsappCommandExcutor.hooklist import Hooklist


class CommandHook:
    def __init__(self):
        self.history = []

    def Hook(self, reciver):
        hook = Hooklist()
        if reciver[-1].startswith("@"):
            # cprint.info(self.history)
            if reciver[-1].split(" ")[0] in hook.hookkey():
                if reciver[-1] in self.history:
                    pass
                else:
                    cprint.info(self.history)
                    cprint.info("command found")
                    cprint.info("Excuting command")
                    data = hook.Hookslist()
                    cprint.ok("Excuting funcation > " + str(data[reciver[-1].split(" ")[0]]))
                    hookfunc = HookFunc()
                    eval("hookfunc." + str(data[reciver[-1].split(" ")[0]]) + "()")
                    self.history.append(reciver[-1])
            else:
                pass
        else:
            pass
