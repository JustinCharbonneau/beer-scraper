from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class Main:

    def __init__(self):

        site = "https://brouehaha.com/our-beers/?lang=en"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, features="lxml")

        beer_names = soup.find_all('h2', class_ = 'c-beer-excerpt__name')

        self.clean_names = []

        for beer_name in beer_names:
            name = str(beer_name)
            self.clean_names.append(name.replace('<h2 class="c-beer-excerpt__name">', "").replace("</h2>", ""))

        with open('beer names/beer_names.txt', 'w') as f:
            for item in self.clean_names:
                f.write("%s\n" % item)


main = Main()
