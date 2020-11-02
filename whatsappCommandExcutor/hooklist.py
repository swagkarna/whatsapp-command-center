# all hook will be in here
# this file will hook the commands with funcations

class Hooklist:

    def Hookslist(self):
        return {
            "@sendmsg": "msg",
            "@deletemsg": "del"
        }

    def hookkey(self):
        return self.Hookslist().keys()
