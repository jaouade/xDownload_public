
from CDownloaderRedTube import DownloaderRedTube

saida = str(input("Pasta de Saída: "))
pesquisa = str(input("Pesquisar por: "))
pgi = int(input("Página Inicial: "))
pgf = int(input("Página final: "))

puxador = DownloaderRedTube(saida, pesquisa, pgi, pgf)
puxador.download()