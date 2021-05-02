import time
import termcolor2
import pyfiglet
from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

print(termcolor2.colored("                                                    Loading", color="green"))
time.sleep(1.2)
three = pyfiglet.figlet_format("3")
print(termcolor2.colored(three, color="yellow"))
time.sleep(1.2)
tow = pyfiglet.figlet_format("2")
print(termcolor2.colored(tow, color="blue"))
time.sleep(1.2)
one = pyfiglet.figlet_format("1")
print(termcolor2.colored(one, color="red"))
time.sleep(1.2)

print(termcolor2.colored("                                                    *Welcome To Our App*", color="cyan"))


def read_from_db():
    try:
        medias = []
        file = open("data.csv", "r")
        file_read = file.read()
        media = file_read.split("\n")
        for i in range(len(media)):
            split = media[i].split(",")
            if split[0] == "Film":
                medias.append(Film(split))
            elif split[1] == "Series":
                medias.append(Series(split))
            elif split[2] == "Documentary":
                medias.append(Documentary(split))
            elif split[3] == "Clip":
                medias.append(Clip(split))

                return medias
    except Exception as e:
        print(termcolor2.colored(f"Error: {e}", color="red"))


medias = read_from_db()


def show_menu():
    menu = ["1_New Media", "2_Search", "3_Edit", "4_Remove", "5_Download"]
    for men in menu:
        print(men)


def add_media():
    menu = ["1_Film", "2_Series", "3_Documentary", "4_Clip"]
    for men in menu:
        print(men, end="  ")
    user = int(input("\nEnter Number: "))
    if user == 1:
        name = input("Enter Name: ")
        director = input("Enter Director: ")
        iMDBScore = int(input("Enter IMDBScore: "))
        url = input("Enter Url: ")
        year = input("Enter Year: ")
        casts = input("Enter Casts: ")
        wf = input("Enter WhatFilm: ")
        medias.append(Film(name, director, iMDBScore, url, year, casts, wf))
    elif user == 2:
        name = input("Enter Name: ")
        director = input("Enter Director: ")
        iMDBScore = int(input("Enter IMDBScore: "))
        url = input("Enter Url: ")
        year = input("Enter Year: ")
        casts = input("Enter Casts: ")
        noe = input("Enter NumberOfEpisodes: ")
        medias.append(Series(name, director, iMDBScore, url, year, casts, noe))
    elif user == 3:
        name = input("Enter Name: ")
        director = input("Enter Director: ")
        iMDBScore = int(input("Enter IMDBScore: "))
        url = input("Enter Url: ")
        year = input("Enter Year: ")
        casts = input("Enter Casts: ")
        doc_abo = input("Enter DocumentaryAbout: ")
        medias.append(Documentary(name, director, iMDBScore, url, year, casts, doc_abo))
    elif user == 4:
        name = input("Enter Name: ")
        director = input("Enter Director: ")
        iMDBScore = int(input("Enter IMDBScore: "))
        url = input("Enter Url: ")
        year = input("Enter Year: ")
        casts = input("Enter Casts: ")
        clipType = input("Enter ClipType: ")
        medias.append(Clip(name, director, iMDBScore, url, year, casts, clipType))


def search():
    user = input("Enter Name Media: ")
    for media in medias:
        if user == media.name:
            media.showInfo()
    else:
        print("Not Exist")


def edit():
    user = input("Enter Name Media: ")
    for media in medias:
        if user == media.name:
            name = input("Enter Name: ")
            director = input("Enter Director: ")
            iMDBScore = int(input("Enter IMDBScore: "))
            url = input("Enter Url: ")
            year = input("Enter Year: ")
            casts = input("Enter Casts: ")
            res = [name, director, iMDBScore, url, year, casts]
            medias.append(res)
    else:
        print("Not Exist")


def remove():
    user = input("Enter Name Media: ")
    for media in medias:
        if user == media.name:
            medias.remove(media)
    else:
        print("Not Exist")


def download():
    user = input("Enter Name Media: ")
    for media in medias:
        if user == media.name:
            Media.download(media)
    else:
        print("Not Exist")


while True:
    show_menu()
    choice = int(input(termcolor2.colored("Enter Choice: ", color="blue")))
    if choice == 1:
        add_media()
    elif choice == 2:
        search()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
    elif choice == 5:
        download()
