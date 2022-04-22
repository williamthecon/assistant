from tkinter import *
from tkinter.font import Font as fn
from tkinter import messagebox as mb
import tkinter as tk
import time as tm
import string as st
import random as rd
import speech_recognition as sr
import pyttsx3 as pt
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uo


from saetze import saetze
from data import * #ar, al
from funcs import funcs
from zeit import zeit, zeit_genau
import commands


eg = pt.init()
eg.setProperty("rate", 150)

text = ""


def reload():
    global vars, text, say, record
    vars = {"text=": text, "say()": say, "record()": record}


def record():
    se = sr.Recognizer()
    try:
        with sr.Microphone() as micro:
            audio = se.listen(micro, timeout=60)
            text = se.recognize_google(audio, language='de_DE')
            return text
    except sr.UnknownValueError:
        return None

def say(text):
    print(text)
    eg.say(text)
    eg.runAndWait()

def check(rc):
    global ar, al
    if rc and ar:
        f = False
        for i in al:
            i += " "
            if rc.startswith(i):
                rc = rc.replace(i, "")
                f = True
        if f:
            return True, rc
        return False, rc
    elif rc:
        return True, rc
    return False, rc

def analize(text):
    for i in commands.all_commands():
        if text.startswith(i):
            print(text)
            print(i)
            text = text.replace(i, "")
            c, p = commands.command(text)



def listen():
    global r
    rc = record()
    r.update()

    v, rc = check(rc)
    if v:
        analize(rc)
    else:
        text = saetze.unbekannt()
        say(text)

def ready():
   global etr, r
   rc = etr.get()

   r.update()

   v, rc = check(rc)
   if v:
       analize(rc)
   else:
       text = saetze.unbekannt()
       say(text)

def main():
    global r, etr, labels
    r = Tk()
    r.title("Assistent")
    r.maxsize(400, 400)
    r.minsize(400, 400)

    ft = fn(r, ("Times New Roman", 17))

    cnv = Canvas(r, width=400, height=400, bg="white")
    cnv.grid(row=0, column=0, rowspan=8, columnspan=5)

    title = Label(r, text="Assistent", bg="white", fg="black", font=ft)
    title.grid(row=0, column=0, columnspan=4)

    etr = Entry(r, font=ft, bg="white", fg="black")
    etr.grid(row=1, column=0, columnspan=4)

    ok = Button(r, text="Ok", font=ft, bg="white", fg="black", command=ready, width=7)
    ok.grid(row=1, column=4)

    ltn = Button(r, text="Listen", font=ft, bg="white", fg="black", command=listen)
    ltn.grid(row=2, column=0, columnspan=3)

    l1 = Label(r, text="", font=ft, bg="white", fg="black")
    l1.grid(row=3, column=0, columnspan=3)

    l2 = Label(r, text="", font=ft, bg="white", fg="black")
    l2.grid(row=4, column=0, columnspan=3)

    l3 = Label(r, text="", font=ft, bg="white", fg="black")
    l3.grid(row=5, column=0, columnspan=3)

    l4 = Label(r, text="", font=ft, bg="white", fg="black")
    l4.grid(row=6, column=0, columnspan=3)

    l5 = Label(r, text="", font=ft, bg="white", fg="black")
    l5.grid(row=7, column=0, columnspan=3)

    labels = [l1, l2, l3, l4, l5]

    r.mainloop()


commands = commands.commands(say, record)
reload()

main()

