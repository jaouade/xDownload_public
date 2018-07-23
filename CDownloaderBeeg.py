from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4
import os
import time
from CConexao import Conexao


class DownloaderBeeg:

    def __init__(self, _pasta_saida, _pesquisa, _pagina_inicial, _pagina_final):
        self.pasta_saida = _pasta_saida
        self.pesquisa = _pesquisa
        self.pg_inicial = _pagina_inicial
        self.pg_final = _pagina_final
        self.i = 1
        self.tent = 0
        self.conexao = Conexao()

    def download(self):
        if self.conexao.get_status():
            url = str('https://www.beeg.com/tag/' + self.pesquisa)

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
                    comando = 'youtube-dl \"' + link + '\"' + ' --output \\' + self.pasta_saida + '\\%(title)s.%(ext)s'
                    os.system(comando)
            except TimeoutException:
                print("Tempo de carregamento esgotado!")
            except:
                os.system("cls")
                print("Tempo limite para o carregamento da página esgotado.")
                print("Tente novamente!")
        else:
            self.tent += 1
            print("Sem conexão... Tentativa " + str(self.tent))
            time.sleep(5)
