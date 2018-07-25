import requests
import bs4
import os
import time
from CConection import Conection


class DownloaderEporner:

    def __init__(self, _output_dir, _search, _first_page, _last_page):
        self.output_dir = _output_dir
        self.search = str(_search).replace("+", "-") # eporner uses - in place + to concatenate strings
        self.first_page = _first_page
        self.last_page = _last_page
        self.i = 1
        self.tent = 0
        self.Conection = Conection()

    def download(self):
        if self.Conection.get_status():
            for self.i in range(self.first_page, self.last_page):
                response = requests.get(str('https://www.eporner.com/search/' + self.search + '/' + str(self.i)) + '/')
                soup = bs4.BeautifulSoup(response.text, "html.parser")
                for div in soup.find_all(class_='mb'):  # mb é a classe de div que contem os links
                    link = "https://www.eporner.com" + str(div.find('a')['href'])
                    comando = 'youtube-dl \"' + link + '\"' + ' --output \\' + self.output_dir + '\\%(title)s.%(ext)s'
                    os.system(comando)
        else:
            self.tent += 1
            print("No conection... " + str(self.tent))
            time.sleep(5)
