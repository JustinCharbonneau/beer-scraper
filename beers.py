from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from unidecode import unidecode
import pickle


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

        self.beer_info = {}
        print('ya!')

        cnt = 0
        # Get description
        for beer_name in self.clean_names:
            cnt += 1
            if cnt == 15:
                break
            print('yo!')
            beer_name = beer_name.replace(" ", "-")
            site = "https://brouehaha.com/beers/" + str(beer_name) + "/?lang=en"
            site = unidecode(site)

            if site == 'https://brouehaha.com/beers/Berliner-Weisse-;-lime-et-noix-de-coco/?lang=en':
                site = 'https://brouehaha.com/beers/Berliner-Weisse-lime-et-noix-de-coco/?lang=en'

            if site == 'https://brouehaha.com/beers/Acidula-Fraise-&amp;-Vanille/?lang=en':
                site = 'https://brouehaha.com/beers/Acidula-Fraise-Vanille/?lang=en'

            print(site)
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(site, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page, features="lxml")


            beer_desc = BeautifulSoup(str(soup.find_all('div', class_='c-beer__description')))
            beer_desc_p = beer_desc.find_all('p')
            if len(beer_desc_p) > 1:
                print(beer_desc_p[1])
                description = beer_desc_p[1]
            else:
                description = ""

            self.beer_info[beer_name] = description
            print(self.beer_info[beer_name])

        with open('beer names/beer_info.pkl', 'wb') as f:
            pickle.dump(self.beer_info, f)

        with open('beer names/beer_info.pkl', 'rb') as config_dictionary_file:

            # Step 3
            config_dictionary = pickle.load(config_dictionary_file)

            # After config_dictionary is read from file
            print(config_dictionary)


main = Main()
