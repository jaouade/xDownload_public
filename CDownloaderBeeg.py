from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import os
import time
from CConection import Conection


class DownloaderBeeg:

    def __init__(self, _output_dir, _search, _first_page, _last_page):
        self.output_dir = _output_dir
        self.search = _search
        self.first_page = _first_page
        self.last_page = _last_page
        self.i = 1
        self.tent = 0
        self.Conection = Conection()

    def download(self):
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
                    comando = 'youtube-dl \"' + link + '\"' + ' --output \\' + self.output_dir + '\\%(title)s.%(ext)s'
                    os.system(comando)
            except TimeoutException:
                print("Tempo de carregamento esgotado!")
            except:
                os.system("cls")
                print("Tempo limite para o carregamento da página esgotado.")
                print("Tente novamente!")
        else:
            self.tent += 1
            print("No conection... " + str(self.tent))
            time.sleep(5)
