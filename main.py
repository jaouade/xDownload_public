
from CDownloaderYouPorn import DownloaderYouPorn

saida = str(input("Pasta de Saída: "))
pesquisa = str(input("Pesquisar por: "))
pgi = int(input("Página Inicial: "))
pgf = int(input("Página final: "))

puxador = DownloaderYouPorn(saida, pesquisa, pgi, pgf)
puxador.download()