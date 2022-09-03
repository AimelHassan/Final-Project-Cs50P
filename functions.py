from csv import *
from email import header
from tkinter import *
from tkinter import messagebox
import sys
import random
import pygame
from tabulate import tabulate
pygame.mixer.init()


class Leaderboard():
    def __init__(self, *args):
        ...

    def show(self):
        ld_lst = []
        with open("LEADERBOARD.csv", "r") as rld:
            reader = DictReader(rld)
            for row in reader:
                ld_lst.append(row)
        pr_ld = tabulate(ld_lst,headers="keys",tablefmt="grid")
        window = Tk()
        window.title("Leaderboard")
        label = Label(window, text=pr_ld,fg="white",bg="black").pack()
        window.mainloop()

    def create(self):
        players=[]
        sorted_lst=[]
        with open("data_entry.csv", "r") as rfile:
            reader = DictReader(rfile)
            for row in reader:
                players.append(row)

            sorted_lst= sorted(players, key=lambda player:int(player["Points"]), reverse=True)
        fieldnames = ["Player","Points"]
        with open("LEADERBOARD.csv", "w+") as ldfile:
            writer = DictWriter(ldfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_lst)



def point_calc(hits):
    points = len(hits)
    return int(points)

def rating(points):
    if points >= 15:
        return "AIM GOD"
    elif points > 10:
        return "Its fine"
    elif points ==5:
        return "Really bro?"
    elif points > 5:
        return "Bro wtf????"

def user_checker(name):
    if name.isalnum():
        return True
    else:
        return False


def user_get_store(points):
    random_names = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "DUMB", "HERO", "PYSCHO"]
    window=Tk()
    window.title("Save")
    window.geometry("320x100")
    main_lst=[]
    ge = pygame.mixer.Sound('Assets/game end.wav')
    window["background"] = "#856ff8"


    def Save():
        try:
            _rating = rating(points)
            uname = name.get()
            if user_checker(uname) == True:
                lst={"Player":uname, "Points": int(points)}
                main_lst.append(lst)
                fieldnames = ["Player", "Points"]
                with open("data_entry.csv", "r") as rfile:
                    reader = DictReader(rfile)
                    for row in reader:
                        if row["Player"] == lst["Player"]:
                            messagebox.showinfo("ERROR", "USERNAME ALREADY EXISTS, RANDOM USER GENERATED...")
                            lst["Player"] = random.choice(random_names) + str(random.randint(1,100))
                        
                with open("data_entry.csv","a") as file:
                    Writer=DictWriter(file, fieldnames=fieldnames)
                    Writer.writerows(main_lst)
                    messagebox.showinfo("Username",f"Player: {uname}, Points: {points}\nRating: {_rating}")
                    ge.play()
            else:
                messagebox.showinfo("ERROR","WRONG FORMAT")
        except ValueError:
            sys.exit("WRONG DATA TYPE PROVIDED")



    label1=Label(window,text="Player: ",padx=20,pady=10, bg='#856ff8',fg="#FFFFFF")
    label2 = Label(window,text="How do we remember you?\nFormat:\n Only alphabets and numbers allowed",padx=20,pady=10,bg="#856ff8",fg="#FFFFFF")


    name=Entry(window,width=20,borderwidth=2)


    save=Button(window,text="Save",padx=10,pady=5,command=Save,bg='#856ff8',fg="#FFFFFF")


    label1.grid(row=0,column=0)
    label2.grid(row=1,column=1)



    name.grid(row=0,column=1)
    save.grid(row=1,column=0)


    window.mainloop()
    print(main_lst)
