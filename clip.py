from media import Media
import termcolor2


class Clip(Media):
    def __init__(self, name="", director="", iMDBScore="", url="", year="", casts="", clipType=""):
        super().__init__(name, director, iMDBScore, url, year, casts)
        self.clipType = clipType

    def show_clip(self):
        print(termcolor2.colored("ShowInfo: ", color="blue"))
        print(
            f"Name: {self.name} \nDirector: {self.director} \nIMDBScore: {self.iMDBScore}"
            f" \nUrl: {self.url}\nYear: {self.year} \ncasts: {self.casts} \nClipType: {self.clipType}")

