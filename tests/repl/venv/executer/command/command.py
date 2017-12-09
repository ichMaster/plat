import json

from executer.command.messanger import *


class error:
    def __init__(self, code:str, msg:str):
        self.error_code = code
        self.error_msg = msg


    def getError(self):
        self.out = {
            self.error_code: self.error_msg
        }
        return self.out

class message:
    def __init__(self, code:str, msg:str):
        self.message_code = code
        self.message_msg = msg


    def getMessage(self):
        self.out = {
            self.message_code: self.message_msg
        }
        return self.out

class command:
    def __init__(self, command_name):
        self.respond = []
        self.command_name = command_name
        self.errors = []
        self.messages = []
        self.output = []
        self.output_header = {}
        self.output_body = {}


    def getOutput(self):
        self.respond.append({"command_name": self.command_name})
        self.respond.append(self.errors)
        self.respond.append(self.messages)
        self.output.append(self.output_header)
        self.output.append(self.output_body)
        self.respond.append(self.output)
        return json.dumps(self.respond)


    def execute(self):
        self.messages.append(message("message", "message text").getMessage())
        self.errors.append(error("error", "error text").getError())
        self.output_header = {
            1: "Name",
            2: "Value",
            3: "Description"
        }
        self.output_body = [
            {"Name": "Bob", "Value": "23", "Description": "Age"},
            {"Name": "Jane", "Value": "59", "Description": "wheight"},
            {"Name": "Nick", "Value": "33", "Description": "Age"}
        ]
        return self.getOutput()

