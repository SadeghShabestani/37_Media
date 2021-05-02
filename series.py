from media import Media
import termcolor2


class Series(Media):
    def __init__(self, name="", director="", iMDBScore="", url="", year="", casts="", noe=""):
        super().__init__(name, director, iMDBScore, url, year, casts)
        self.number_of_episodes = noe

    def show_Series(self):
        print(termcolor2.colored("ShowInfo: ", color="blue"))
        print(
            f"Name: {self.name} \nDirector: {self.director} \nIMDBScore: {self.iMDBScore} \nUrl: {self.url}"
            f" \nYear: {self.year} \ncasts: {self.casts} \nNumberOfEpisodes: {self.number_of_episodes}")


