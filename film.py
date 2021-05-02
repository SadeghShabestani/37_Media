from media import Media
import termcolor2


class Film(Media):
    def __init__(self, name="", director="", iMDBScore="", url="", year="", casts="", wf=""):
        super().__init__(name, director, iMDBScore, url, year, casts)
        self.whatFilm = wf

    def show_film(self):
        print(termcolor2.colored("ShowInfo: ", color="blue"))
        print(
            f"Name: {self.name} \nDirector: {self.director} \nIMDBScore: {self.iMDBScore} \nUrl: {self.url}"
            f" \nYear: {self.year} \ncasts: {self.casts} \nWhatFilm: {self.whatFilm}")

