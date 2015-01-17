# -*- coding: utf-8 -*-

from makore.fetchers.base import HTMLHeadLineFetcher
import re

__author__ = 'quatrix'


class Haaretz(HTMLHeadLineFetcher):
    __url__ = "http://haaretz.co.il"
    __favicon__ = "http://haaretz.co.il/favicon.ico"
    __publisher__ = "הארץ"

    @property
    def headline(self):
        if not hasattr(self, "_headline"):
            self._headline = self.html.find_all("article", attrs={"data-back": re.compile(r"headline--")})[0]
        return self._headline

    @property
    def text(self):
        return self.headline.h1.text
        
    @property
    def url(self):
        return self.__url__ + self.headline.a.get("href")

    @property
    def image(self):
        return self.__url__ + self.headline.img.get("srcset")


