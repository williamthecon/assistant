from funcs import funcs
from rechner import rechner
from stadt_daten import data


class commands:
    def __init__(self, say, record):
        self.stop = {
            "commands": ["stope das Programm", "beende das Programm", "breche das Programm ab", "stoppe", "beenden", "stop", "beende", "breche ab"],
            "func": funcs.stop,
            "args": ["say()"]
        }
        self.shutdown = {
            "commands": ["shutdown the computer", "shutdown the laptop", "shutdown all", "shutdown", "herunterfahren", "fahre herunter", "fahre den Computer herunter", "fahre den Laptop herunter", "fahre dich herunter"],
            "func": funcs,
            "args": ["text=", "say()", "record()"]
        }
        self.restart = {
            "commands": [],
            "func": funcs,
            "args": ["text=", "say()", "record()"]
        }
        self.logout = {
            "commands": [],
            "func": funcs,
            "args": ["text=", "say()", "record()"]
        }
        self.rechnen = {
            "commands": [],
            "func": funcs.rechner,
            "args": ["text=", "say()"]
        }
        self.commands = {
            "stop": self.stop,
            "shutdown": self.shutdown,
            "restart": self.restart,
            "logout": self.logout
        }
        self.keys = {}
        for commands, func, args in self.commands.values():
            for command in commands:
                self.keys[command] = [func, args]
        print(self.commands["stop"])

    def all_commands(self):
        return self.keys.keys()

    def command(self, c):
        return self.keys[c]