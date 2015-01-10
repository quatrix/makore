from __future__ import absolute_import
import sys
from makore.fetchers.haaretz import Haaretz
from makore.fetchers.walla import Walla
from makore.fetchers.ynet import Ynet
from jinja2 import Environment, PackageLoader


__author__ = 'quatrix'


if __name__ == "__main__":
    env = Environment(loader=PackageLoader('makore', 'templates'))
    template = env.get_template('main.html')


    headlines = [
        {"provider": "haaretz", "headline": Haaretz().get_headline()},
        {"provider": "walla", "headline": Walla().get_headline()},
        {"provider": "ynet", "headline": Ynet().get_headline()},
    ]

    html = template.render(headlines=headlines)

    open(sys.argv[1], "w").write(html.encode("utf-8"))
