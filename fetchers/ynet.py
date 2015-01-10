from makore.fetchers.base import HTMLHeadLineFetcher

__author__ = 'quatrix'

class Ynet(HTMLHeadLineFetcher):
    __url__ = "http://ynet.co.il"

    @property
    def headline(self):
        if not hasattr(self, "_headline"):
            self._headline = self.html.find(id="cmpTopStory")
        return self._headline

    @property
    def text(self):
        return self.headline.find_all("a")[1].text

    @property
    def url(self):
        return self.__url__ + self.headline.find_all("a")[0].get("href")

    @property
    def image(self):
        return self.headline.img.get("src")
