# -*- coding: utf-8 -*-

from makore.fetchers.base import HTMLHeadLineFetcher
import re

__author__ = 'quatrix'

class Ynet(HTMLHeadLineFetcher):
    __url__ = "http://ynet.co.il"
    __favicon__ = "http://ynet.co.il/favicon.ico"
    __publisher__ = "וויינט"

    @property
    def headline(self):
        if not hasattr(self, "_headline"):
            self._headline = self.html.find(id="cmpTopStory")
        return self._headline


    @property
    def headline_anchor(self):
        return self.headline.find_all("a", attrs={"class": re.compile(r".*header")})[0]

    @property
    def text(self):
        return self.headline_anchor.text

    @property
    def url(self):
        return self.__url__ + self.headline_anchor.get("href")

    @property
    def image(self):
        return self.headline.find("img", attrs={"title": re.compile(".+")}).get("src")
