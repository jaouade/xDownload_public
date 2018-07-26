from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import os
import time
from CConection import Conection
import json
import io


class DownloaderBeeg:

    def __init__(self, _output_dir, _search, _first_page, _last_page):
        self.output_dir = _output_dir
        self.search = _search
        self.first_page = _first_page
        self.last_page = _last_page
        self.i = 1
        self.j = 1
        self.Conection = Conection()
        self.list_link = []

    def download(self):
        self.list_link = self.get_list_link()
        if self.list_link != 0:
            for j in range(0, len(self.get_list_link())):
                self.json_details_write(len(self.list_link), j, self.list_link[j])
                command = 'youtube-dl \"' + self.list_link[j] + '\"' + ' --output \\' + self.output_dir + '\\%(title)s.%(ext)s'
                os.system(command)

    def get_list_link(self):
        if self.Conection.get_status():
            url = str('https://www.beeg.com/tag/' + self.search)

            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            driver = webdriver.Chrome(chrome_options=options)
            try:
                driver.get(url)
                print("Aguardando carregamento em 20s ...")
                time.sleep(20)
                html = driver.page_source
                soup = bs4.BeautifulSoup(html, "html.parser")
                for div in soup.find_all(class_='thumb-unit'):  # thumb-unit é a classe de div que contem os links
                    link = "https://beeg.com" + str(div.find('a')['href'])
                    self.list_link.append(link)
                return self.list_link
            except TimeoutException:
                print("Tempo de carregamento esgotado!")
            except:
                os.system("cls")
                print("Tempo limite para o carregamento da página esgotado.")
                print("Tente novamente!")
        else:
            print("No conection... ")
            return 0

    # writing a json file to the graphic layer

    def json_details_write(self, _list_size, _current_number, _current_link):
        percent = (_current_number/_list_size)*100  # percent calc
        # Define data
        data = {'%': percent,
                'range': _list_size,
                'current': _current_number,
                'link': _current_link}
        # Write JSON file
        with io.open('data.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)