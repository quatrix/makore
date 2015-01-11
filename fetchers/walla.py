from makore.fetchers.base import HTMLHeadLineFetcher

__author__ = 'quatrix'

class Walla(HTMLHeadLineFetcher):
    __url__ = "http://news.walla.co.il"
    __favicon__ = "http://walla.co.il/favicon.ico"

    @property
    def headline(self):
        if not hasattr(self, "_headline"):
            self._headline = self.html.find_all("article", attrs={"class": "article fc main-article"})[0]
        return self._headline

    @property
    def text(self):
        return self.headline.find("span", attrs={"class": "text"}).text

    @property
    def url(self):
        return self.__url__ + self.headline.find("a", attrs={"class": "event"}).get("href")

    @property
    def image(self):
        return self.headline.img.get("src")
