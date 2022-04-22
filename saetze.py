import random


class saetze:
    def __init__(self):
        unbekannt = ["Entschuldigung, aber vielleicht habe ich dich nicht richtig verstanden.", "Es tut mir leid, aber da kann ich dir nicht weiterhelfen.",
                          "Tut mir leid, aber damit kann ich nichts anfangen.", "Das ist keiner der festgelegten Befehle.", "Bitte versuche es erneut oder benutze einen anderen Befehl.",
                          "Das konnte ich leider nicht verstehen.", "Kann es sein, dass du dich versprochen hast?", "Tut mir leid, aber das musst du noch einmal versuchen.",
                          "Bitte benutze einen anderen Befehl.", "Kannst du das bitte noch einmal wiederholen?"]
        self.saetze = {"unbekannt": unbekannt}

    def satz(self, typ):
        try:
            x = self.saetze[typ]
            return x
        except:
            return None

    def unbekannt(self):
        return random.choice(self.saetze["unbekannt"])


saetze = saetze()