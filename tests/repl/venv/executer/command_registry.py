from executer.command.messanger import messanger


class command_registry:
    def __init__(self):
        self.commands = {
            "exit": "COMMAND_EXIT",
            "help": "COMMAND_HELP",
            "set": "COMMAND_SET",
            "get": "COMMAND_GET",
            "ls": "COMMAND_LS",
            "cd": "COMMAND_CD",
            "cat": "COMMAND_CAT"
        }


    def getCommnad(self, command:str):
        if command in self.commands.keys():
            return self.commands[command]
        else:
            m = messanger()
            return m.getMessage("ERR_COMMANDNOTFOUD")