from __future__ import absolute_import
import sys
from makore.fetchers.haaretz import Haaretz
from makore.fetchers.walla import Walla
from makore.fetchers.ynet import Ynet
from jinja2 import Environment, PackageLoader
import json


__author__ = 'quatrix'


if __name__ == "__main__":
    env = Environment(loader=PackageLoader('makore', 'templates'))
    template = env.get_template('main.html')

    headlines = [
        Haaretz().get_headline(),
        Walla().get_headline(),
        Ynet().get_headline(),
    ]

    html = template.render(headlines=headlines)

    print(json.dumps(headlines, indent=4))
    open(sys.argv[1], "w").write(html.encode("utf-8"))
