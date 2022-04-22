import time, datetime


def st(s):
    return time.strftime(s)

class umformen:
    def __init__(self):
        self.wt = {"Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch", "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag", "Sunday": "Sonntag"}

    def wochentag(self, t):
        try:
            x = self.wt[t]
            return x
        except:
            return None

    def stunden(self, t):
        return t - 12

    def uhr(self, stunden, minuten, sekunden, uhr=None):
        if uhr is None:
            uhr = False
        if sekunden >= 30:
            minuten += 1
        s = False
        if stunden > 12:
            stunden = self.stunden(stunden)
            s = True
        if minuten == 0:
            x = f"{stunden}" if not uhr else f"{stunden} Uhr"
        elif 0 < minuten < 4 or 57 < minuten < 60:
            x = f"kurz nach {stunden}" if not uhr else f"kurz nach {stunden} Uhr"
        elif 3 < minuten < 8:
            x = f"ungefähr 5 Minuten nach {stunden}" if not uhr else f"ungefähr 5 Minuten nach {stunden} Uhr"
        elif 7 < minuten < 13:
            x = f"ungefähr 10 Minuten nach {stunden}" if not uhr else f"ungefähr 10 Minuten nach {stunden} Uhr"
        elif 12 < minuten < 18:
            x = f"ungefähr viertel nach {stunden}"
        elif 17 < minuten < 23:
            x = f"ungefähr 20 Minuten nach {stunden}" if not uhr else f"ungefähr 20 Minuten nach {stunden} Uhr"
        elif 22 < minuten < 27:
            x = f"ungefähr 25 Minuten nach {stunden}" if not uhr else f"ungefähr 25 Minuten nach {stunden} Uhr"
        elif 26 < minuten < 33:
            x = f"ungefähr halb {stunden}"
        elif 32 < minuten < 38:
            x = f"ungefähr 25 Minuten vor {stunden+1}" if not uhr else f"ungefähr 25 Minuten vor {stunden+1} Uhr"
        elif 37 < minuten < 43:
            x = f"ungefähr 20 Minuten vor {stunden+1}" if not uhr else f"ungefähr 20 Minuten vor {stunden+1} Uhr"
        elif 42 < minuten < 48:
            x = f"ungefähr viertel vor {stunden+1}" if not uhr else f"ungefähr viertel vor {stunden+1} Uhr"
        elif 47 < minuten < 53:
            x = f"ungefähr 10 Minuten vor {stunden+1}" if not uhr else f"ungefähr 10 Minuten vor {stunden+1} Uhr"
        elif 52 < minuten < 58:
            x = f"ungefähr 5 Minuten vor {stunden+1}" if not uhr else f"ungefähr 5 Minuten vor {stunden+1} Uhr"
        else:
            x = None

        return x


class get:
    def wochentag(self):
        return umformen.wochentag(st("%A"))

    def monatstag(self):
        return st("%d")

    def monat(self):
        return st("%m")

    def jahr(self):
        return st("%Y")

    def uhr(self):
        stunden = int(st("%H"))
        minuten = int(st("%M"))
        sekunden = int(st("%S"))
        x = umformen.uhr(stunden, minuten, sekunden)
        return x

    def uhr_genau(self):
        stunden = int(st("%H"))
        minuten = int(st("%M"))
        sekunden = int(st("%S"))
        x = f"{stunden}:{minuten}:{sekunden}"
        return x


umformen = umformen()
get = get()


def zeit():
    x = f"Heute ist {get.wochentag()}, der {get.monatstag()}.{get.monat()}.{get.jahr()}, und es ist {get.uhr()}."
    return x

def zeit_genau():
    x = f"Heute ist {get.wochentag()}, der {get.monatstag()}.{get.monat()}.{get.jahr()}, und es ist {get.uhr_genau()}."
    return x
