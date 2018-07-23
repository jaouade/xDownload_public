import sys
from CDownloaderXvideos import DownloaderXvideos
from CDownloaderYouPorn import DownloaderYouPorn
from CDownloaderRedTube import DownloaderRedTube
# ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida

servidor = str(sys.argv[1])
pesquisa = str(sys.argv[2])
pagina_ini = int(sys.argv[3])
pagina_fin = int(sys.argv[4])
pasta_saida = str(sys.argv[5])

if servidor == 'XVideos':
    print("-----------------------------------------------------------")
    print("Servidor: XVideos" )
    print("Pesquisa: " + pesquisa)
    print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
    print("-----------------------------------------------------------")
    puxador = DownloaderXvideos(pasta_saida, pesquisa, pagina_ini, pagina_fin)
    puxador.download()
elif servidor == 'YouPorn':
    print("-----------------------------------------------------------")
    print("Servidor: YouPorn" )
    print("Pesquisa: " + pesquisa)
    print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
    print("-----------------------------------------------------------")
    puxador = DownloaderYouPorn(pasta_saida, pesquisa, pagina_ini, pagina_fin)
    puxador.download()
elif servidor == 'RedTube':
    print("-----------------------------------------------------------")
    print("Servidor: RedTube" )
    print("Pesquisa: " + pesquisa)
    print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
    print("-----------------------------------------------------------")
    puxador = DownloaderRedTube(pasta_saida, pesquisa, pagina_ini, pagina_fin)
    puxador.download()
else:
    print('Servidor Inválido')