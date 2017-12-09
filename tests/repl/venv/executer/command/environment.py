from executer.command.messanger import messanger


class environment:
    def __init__(self):
        self.variables = {
            "PROMPT_PRE": "$> ",
            "PROMPT_POST": " >> ",
            "PROMPT": "",
            "CURRENT_COMMAND": "",
            "CURRENT_DIRRECTORY": "."
        }


    def getVariable(self, code:str = None):
        if code in self.variables.keys():
            return self.variables[code]
        else:
            m = messanger()
            return m.getMessage("ERR_VARNOTFOUND")


    def setVariable(self, code:str, value:str):
        if code in self.variables.keys():
            self.variables[code] = value
        else:
            m = messanger()
            return m.getMessage("ERR_VARNOTFOUND")


    def setCurrentCommand(self, dir: str):
        self.variables["CURRENT_COMMAND"] = dir


    def getCurrentCommand(self):
        return self.variables["CURRENT_COMMAND"]


    def setCurrentDirectory(self, dir:str):
        self.variables["CURRENT_DIRRECTORY"] = dir


    def getCurrentDirectory(self):
        return self.variables["CURRENT_DIRRECTORY"]


    def setPrompt(self, prefix:str = None, postfix:str = None):
        if  prefix != None:
            self.setVariable("PROMPT_PRE", prefix)
        if postfix != None:
            self.setVariable("PROMPT_POST", postfix)
        self.setVariable("PROMPT", self.variables["PROMPT_PRE"] + self.getCurrentDirectory() + self.variables["PROMPT_POST"])


    def getPrompt(self):
        return self.variables["PROMPT"]
