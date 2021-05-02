import termcolor2
import pytube
from actor import Actor


class Media:
    def __init__(self, name, director, iMDBScore, url, year, casts):
        self.name = name
        self.director = director
        self.iMDBScore = iMDBScore
        self.url = url
        self.year = year
        self.casts = casts

    def showInfo(self):
        print(termcolor2.colored("ShowInfo: ", color="blue"))
        print(
            f"Name: {self.name} \nDirector: {self.director} \nIMDBScore: {self.iMDBScore}"
            f" \nUrl: {self.url}\nYear: {self.year} \ncasts: {self.casts}")

    def casts(self):
        actor = self.casts.split(" ")
        for acto in actor:
            Actor(acto).show_actor()

    def download(self):
        pytube.YouTube(self.url).streams.first().download()
        print(termcolor2.colored("Done: ", color="green"))
