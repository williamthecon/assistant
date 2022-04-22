import os
from data import * #ar, al, pw


class funcs:
    def stop(self, args):
        say = args[0]
        say("Das Programm wird gestoppt.")
        quit()

    def shutdown(self, args):
        text, say, record = arg
        text = text.replace(" ", "")
        if text.lower() == pw["sec"]:
            os.system("shutdown /s /t 1")
            return
        say("Bist du sicher, dass du den PC herunterfahren möchtest?")
        r = record()
        if r and ar:
            v = False
            for a in ar:
                if r.startswith(a):
                    r = r.replace(a, "")
                    v = True
                    break
            if not v:
                return
            if r in ["ja", "ja bitte"]:
                say("Der Computer wird heruntergefahren.")
                os.system("shutdown /s /t 1")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return
        elif r:
            if r in ["ja", "ja bitte"]:
                os.system("shutdown /s /t 1")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return

    def restart(self, args):
        text, say, record = arg
        text = text.replace(" ", "")
        if text.lower() == pw["sec"]:
            os.system("shutdown /r /t 1")
            return
        say("Bist du sicher, dass du den PC neu starten möchtest?")
        r = record()
        if r and ar:
            v = False
            for a in ar:
                if r.startswith(a):
                    r = r.replace(a, "")
                    v = True
                    break
            if not v:
                return
            if r in ["ja", "ja bitte"]:
                say("Der Computer wird neu gestartet.")
                os.system("shutdown /r /t 1")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return
        elif r:
            if r in ["ja", "ja bitte"]:
                os.system("shutdown /r /t 1")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return

    def logout(self, args):
        text, say, record = arg
        text = text.replace(" ", "")
        if text.lower() == pw["sec"]:
            os.system("shutdown -l")
            return
        say("Bist du sicher, dass du dich abmelden möchtest?")
        r = record()
        if r and ar:
            v = False
            for a in ar:
                if r.startswith(a):
                    r = r.replace(a, "")
                    v = True
                    break
            if not v:
                return
            if r in ["ja", "ja bitte"]:
                say("Du wirst abgemeldet")
                os.system("shutdown -l")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return
        elif r:
            if r in ["ja", "ja bitte"]:
                os.system("shutdown -l")
            elif r in ["nein", "nein danke", "auf keinen Fall", "abbrechen", "beenden", "stop"]:
                return

    def rechner(self, args):
        text, say = args
        x = rechner(text)
        say(x)


funcs = funcs()
