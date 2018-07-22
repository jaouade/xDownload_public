
from CDownloaderXvideos import DownloaderXvideos

saida = str(input("Pasta de Saída: "))
pesquisa = str(input("Pesquisar por: "))
pgi = int(input("Página Inicial: "))
pgf = int(input("Página final: "))

puxador = DownloaderXvideos(saida, pesquisa, pgi, pgf)
puxador.download()