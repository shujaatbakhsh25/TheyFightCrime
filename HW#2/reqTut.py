import requests
from html.parser import HTMLParser

his = []
hers = []


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.currentTag = None

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.currentTag = tag
        else:
            pass

    def handle_data(self, data):
        if self.currentTag == "p" and data.startswith('He'):
            his.append(data)
            # hers.append(data.split('.')[1])

    def clean(self):
        self.reset()


myParser = MyHTMLParser()
for i in range(50):
    r = requests.get("https://theyfightcrime.org")
    myParser.feed(r.text)
    myParser.clean()

for i in his:
    print(i)
