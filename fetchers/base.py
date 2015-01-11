from bs4 import BeautifulSoup

import requests

__author__ = 'quatrix'


class HTMLHeadLineFetcher(object):
    @property
    def _html(self):
        r = requests.get(self.__url__)
        r.encoding = "utf-8"
        return r.text

    
    @property
    def html(self):
        return BeautifulSoup(self._html)

    def get_headline(self):
        return {
            "text": self.text,
            "url": self.url,
            "image": self.image,
            "icon": self.__favicon__
        }
