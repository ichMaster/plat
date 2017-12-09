class messanger:
    def __init__(self):
        self.messageCodes = {
            "MSG_HELLO": 1,
            "MSG_EXIT": 2
        }

        self.messages = {
            1: "REPL Command Processing",
            2: "Exit from REPL Command Processing"
        }

        self.errorCodes = {
            "ERR_COMMANDNOTFOUD": 1,
            "ERR_FILENOTFOUND": 2,
            "ERR_WRONGDIR": 3,
            "ERR_VARNOTFOUND": 4
        }

        self.errors = {
            1: "Command not found",
            2: "File not found",
            3: "Could not change the directory",
            4: "Enviroment variable is not found"
        }

        self.error_promt = "ERROR CODE:"

    def getMessage(self, code:str = None):
        out = ""
        if  code[:3] == "MSG":
            out = self.messages[self.messageCodes[code]]
        elif code[:3] == "ERR":
            out = self.error_promt + str(self.errorCodes[code]) + " " + self.errors[self.errorCodes[code]]
        return out



