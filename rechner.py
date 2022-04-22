import string, math


def rechner(inp, info=False):
    valid = [i for i in string.digits]
    for i in ["+", "-", "*", "/", "(", ")", "<", ">", "."]:
        valid.append(i)
    operators = ["+", "-", "*", "/"]

    inp = inp.replace(" ", "")

    for i in inp:
        if i not in valid:
            quit("Invalid symbol: %s" % i)
    rechnung = [""]
    nr = 0
    nrs = [0]
    nwr = None
    special = [False]
    if inp.find("(") != -1:
        if inp.find(")") != -1:
            for i in inp:
                print(f"i: {i}") if info else None
                if nwr is None:
                    r = rechnung
                    if len(nrs) - 1 >= nr:
                        for j in nrs[:nr]:
                            r = r[j]
                else:
                    r = nwr
                print(f"r: {r}") if info else None
                if i in string.digits or i == ".":
                    r[-1] += i
                elif i in operators and not special[-1]:
                    r.append(i)
                    r.append("")
                    nrs[-1] += 2
                elif i in operators and special[-1]:
                    r[-1] += i
                elif i == "<":
                    special[-1] = True
                elif i == ">":
                    special[-1] = False
                elif i == "(":
                    nr += 1
                    nrs.append(0)
                    special.append(False)
                    r[-1] = [""]
                elif i in ")":
                    nr -= 1
                    nrs.remove(nrs[-1])
                    special.remove(special[-1])
                    nwr = rechnung
                    for j in nrs[:nr]:
                        nwr = nwr[j]
                    nwr[nrs[-1]] = r
        else:
            quit("On '(' has to follow ')' anywhere")
    else:
        for i in inp:
            print(f"i: {i}") if info else None
            r = rechnung
            print(f"r: {r}") if info else None
            if i in string.digits or i == ".":
                r[-1] += i
            elif i in operators and not special[-1]:
                r.append(i)
                r.append("")
                nrs[-1] += 2
            elif i in operators and special[-1]:
                r[-1] += i
            elif i == "<":
                special[-1] = True
                r.append("<")
                nrs[-1] += 1
            elif i == ">":
                special[-1] = False
                r[-1] += ">"
                nrs[-1] += 1

    for i in range(rechnung.count("")):
        rechnung.remove("")
    print(f"rechnung: {rechnung}") if info else None
    listenstellen = []
    nr = 0
    for i in rechnung:
        if type(i) == list:
            if list not in [type(j) for j in i]:
                listenstellen.append(nr)
            else:
                listenstellen.append([nr])
                nr2 = 0
                for j in rechnung:
                    if type(j) == list:
                        if list not in [type(k) for k in j]:
                            listenstellen[nr].append(nr2)
                        else:
                            listenstellen[nr].append([nr2])
                            nr3 = 0
                            for k in rechnung:
                                if type(k) == list:
                                    if list not in [type(m) for m in k]:
                                        listenstellen[nr][nr2].append(nr3)
                                    else:
                                        listenstellen[nr][nr2].append([nr3])
                                        nr4 = 0
                                        for m in rechnung:
                                            if type(m) == list:
                                                if list not in [type(n) for n in m]:
                                                    listenstellen[nr][nr2][nr3].append(nr4)
                                                else:
                                                    listenstellen[nr][nr2][nr3].append([nr4])
                                                    nr5 = 0
                                                    for n in rechnung:
                                                        if type(n) == list:
                                                            if list not in [type(b) for b in n]:
                                                                listenstellen[nr][nr2][nr3][nr4].append(nr5)
                                                            else:
                                                                listenstellen[nr][nr2][nr3][nr4].append([nr5])
                                                                nr6 = 0
                                                                for b in rechnung:
                                                                    if type(b) == list:
                                                                        if list not in [type(v) for v in b]:
                                                                            listenstellen[nr][nr2][nr3][nr4][nr5].append(
                                                                                nr6)
                                                                        else:
                                                                            quit(
                                                                                "Du hast zu viele Einklammerungen ineinander")
                                                                    nr6 += 1
                                                        nr5 += 1
                                            nr4 += 1
                                nr3 += 1
                    nr2 += 1
        nr += 1
    print(f"listenstellen: {listenstellen}") if info else None
    while list in [type(i) for i in rechnung]:
        print("list in listenstellen") if info else None
        for i in listenstellen:
            print(f"Listenstellen an der Stelle: {i}") if info else None
            if type(i) != list:
                print(f"Typ von {i}: not list") if info else None
                l = rechnung[i]
                print(f"l: {' '.join(l)}") if info else None
                e = []
                mal = False
                geteilt = False
                for j in l:
                    print(f"l an der Stelle: {j}") if info else None
                    if j == "*":
                        print(f"j: *")
                        last = e[-1]
                        e = e[:-1]
                        mal = True
                    elif j == "/":
                        print(f"j: /")
                        last = e[-1]
                        e = e[:-1]
                        geteilt = True
                    elif mal:
                        print(f"mal: True") if info else None
                        print(f"ergebnis: {float(last) * float(j)}") if info else None
                        e.append(str(float(last) * float(j)))
                        mal = False
                    elif geteilt:
                        print(f"geteilt: True") if info else None
                        print(f"ergebnis: {float(last) / float(j)}") if info else None
                        e.append(str(float(last) / float(j)))
                        geteilt = False
                    else:
                        print(f"j: {j}") if info else None
                        if j.startswith("<") and j.endswith(">"):
                            j = j.replace("<", "").replace(">", "")
                            if j.find("*") != -1:
                                j = j.split("*")
                                e.append(float(j[0])**float(j[1]))
                            else:
                                x = float(j.replace("/", ""))
                                x = math.sqrt(x)
                                e.append(x)
                        else:
                            e.append(j)
                print(f"e: {' '.join([str(k) for k in e])}") if info else None
                r = float(e[0])
                op = ""
                for j in e[1:]:
                    print(f"e an der Stelle: {j}") if info else None
                    print(f"r: {r}") if info else None
                    if j in ["+", "-"]:
                        print("j: operator") if info else None
                        op = j
                    elif op == "+":
                        print("op: +")
                        r += float(j)
                        op = ""
                    elif op == "-":
                        print("op: -")
                        r -= float(j)
                        op = ""
                    else:
                        quit("Fehler bei: " + op + str(j) + "\n" + " ".join([str(k) for k in e]))
                print(f"r: {r}") if info else None
                rechnung[i] = str(r)
            else:
                print(f"Typ von {i}: list") if info else None
                l = rechnung
                for j in i:
                    l = l[j]
                e = []
                mal = False
                geteilt = False
                for j in l:
                    if j == "*":
                        last = e[-1]
                        e = e[:-1]
                        mal = True
                    elif j == "/":
                        last = e[-1]
                        e = e[:-1]
                        geteilt = True
                    elif mal:
                        print(f"mal: True") if info else None
                        print(f"ergebnis: {float(last) * float(j)}") if info else None
                        e.append(str(float(last) * float(j)))
                        mal = False
                    elif geteilt:
                        print(f"geteilt: True") if info else None
                        print(f"ergebnis: {float(last) / float(j)}") if info else None
                        e.append(str(float(last) / float(j)))
                    else:
                        print(f"j: {j}") if info else None
                        if j.startswith("<") and j.endswith(">"):
                            j = j.replace("<", "").replace(">", "")
                            if j.find("*") != -1:
                                j = j.split("*")
                                e.append(float(j[0])**float(j[1]))
                            else:
                                x = float(j.replace("/", ""))
                                x = math.sqrt(x)
                                e.append(x)
                        else:
                            e.append(j)
                r = 0
                op = ""
                for j in e:
                    if j in ["+", "-"]:
                        op = j
                    elif op == "+":
                        r += float(j)
                        op = ""
                    elif op == "-":
                        r -= float(j)
                        op = ""
                    else:
                        quit("Fehler bei: " + op + j)
                nr = i[-1]
                i = i[:-1]
                l = rechnung
                for j in i:
                    l = l[j]
                l[nr] = str(r)

    l = rechnung
    print(f"l: {' '.join(l)}") if info else None
    e = []
    mal = False
    geteilt = False
    for j in l:
        print(f"l an der Stelle: {j}") if info else None
        if j == "*":
            print(f"j: *") if info else None
            last = e[-1]
            e = e[:-1]
            mal = True
        elif j == "/":
            print(f"j: /") if info else None
            last = e[-1]
            e = e[:-1]
            geteilt = True
        elif mal:
            print(f"mal: True") if info else None
            print(f"rechnung: {float(last)} * {float(j)}") if info else None
            print(f"ergebnis: {float(last) * float(j)}") if info else None
            e.append(str(float(last) * float(j)))
            mal = False
        elif geteilt:
            print(f"geteilt: True") if info else None
            print(f"rechnung: {float(last)} / {float(j)}") if info else None
            print(f"ergebnis: {float(last) / float(j)}") if info else None
            e.append(str(float(last) / float(j)))
        else:
            print(f"j: else: {j}") if info else None
            if j.startswith("<") and j.endswith(">"):
                j = j.replace("<", "").replace(">", "")
                if j.find("*") != -1:
                    j = j.split("*")
                    e.append(float(j[0])**float(j[1]))
                else:
                    x = float(j.replace("/", ""))
                    x = math.sqrt(x)
                    e.append(x)
            else:
                e.append(j)
    print(f"e: {', '.join([str(k) for k in e])}") if info else None
    print(f"e: {type(e)}") if info else None
    if e[0] in operators:
        r = float("".join(e[:2]))
        e[1] = e[0] + e[1]
        e = e[1:]
    else:
        r = float(e[0])
    print(f"r: {r}") if info else None
    op = ""
    for j in e[1:]:
        print(f"e an der Stelle: {j}") if info else None
        print(f"r: {r}") if info else None
        if j in ["+", "-"]:
            print("j: operator") if info else None
            op = j
        elif op == "+":
            print("op: +") if info else None
            r += float(j)
            op = ""
        elif op == "-":
            print("op: -") if info else None
            r -= float(j)
            op = ""
        else:
            quit("Fehler bei: " + op + str(j) + "\n" + " ".join([str(k) for k in e]))
    return r
