# -*- coding: utf-8 -*-

from __future__ import absolute_import
import sys
from makore.fetchers.haaretz import Haaretz
from makore.fetchers.walla import Walla
from makore.fetchers.ynet import Ynet
from jinja2 import Environment, PackageLoader
import json


__author__ = 'quatrix'

headlines = json.loads(
"""
[
    {
        "publisher": "הארץ",
        "url": "http://haaretz.co.il/news/politics/.premium-1.2540753",
        "text": "דאעש עושה פעלולי יחצ, אך פוטנציאל הנזק של אל-קאעדה למערב רב יותר",
        "image": "http://haaretz.co.il/polopoly_fs/1.2540752.1421357079!/image/774342073.jpg_gen/derivatives/size_552x313/774342073.jpg",
        "date": "15:21",
        "icon": "http://haaretz.co.il/favicon.ico"
    },
    {
        "publisher": "וואלה",
        "url": "http://news.walla.co.il/item/2820671",
        "text": "המאבק בטרור: 4 נעצרו ביוון בחשד שהשתייכו לתא הבלגי",
        "image": "http://msc.wcdn.co.il/w/w-500/1840006-54.jpg",
        "date": "15:21",
        "icon": "http://walla.co.il/favicon.ico"
    },
    {
        "publisher": "וויינט",
        "url": "http://ynet.co.il/articles/0,7340,L-4616045,00.html",
        "text": "ראש המנהל קידם מגדל בתא ופרויקט בדרום",
        "image": "http://images1.ynet.co.il/PicServer4/2015/01/17/5822665/582266301000100396220.jpg",
        "date": "15:21",
        "icon": "http://ynet.co.il/favicon.ico"
    }
]

""")

if __name__ == "__main__":
    env = Environment(loader=PackageLoader('makore', 'templates'))
    template = env.get_template('main.html')

    """
    headlines = [
        Haaretz().get_headline(),
        Walla().get_headline(),
        Ynet().get_headline(),
    ]
    """

    html = template.render(headlines=headlines)

    print(json.dumps(headlines, indent=4))
    open(sys.argv[1], "w").write(html.encode("utf-8"))
