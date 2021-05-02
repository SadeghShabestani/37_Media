from media import Media
import termcolor2


class Documentary(Media):
    def __init__(self, name="", director="", iMDBScore="", url="", year="", casts="", da=""):
        super().__init__(name, director, iMDBScore, url, year, casts)
        self.documentary_about = da

    def show_documentary(self):
        print(termcolor2.colored("ShowInfo: ", color="blue"))
        print(
            f"Name: {self.name} \nDirector: {self.director} \nIMDBScore: {self.iMDBScore} \nUrl: {self.url}"
            f" \nYear: {self.year} \ncasts: {self.casts} \nDocumentaryAbout: {self.documentary_about}")

