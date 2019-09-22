import requests
from html.parser import HTMLParser
import os


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
        if self.currentTag == "p" and data.startswith("He"):
            she = data.find("She")
            end = data.find("They")
            with open('his.txt', 'a+') as f:
                f.write(data[0:she]+"\n")
            with open('her.txt', 'a+') as f:
                f.write(data[she:end]+"\n")

    def clean(self):
        self.reset()


if __name__ == "__main__":
    if os.path.exists('his.txt'):
        os.remove('his.txt')
    if os.path.exists('her.txt'):
        os.remove('her.txt')
    myParser = MyHTMLParser()
    for i in range(50):
        r = requests.get("https://theyfightcrime.org")
        myParser.feed(r.text)
        myParser.clean()
