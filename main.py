import sys
from CDownloaderXvideos import DownloaderXvideos
from CDownloaderYouPorn import DownloaderYouPorn
from CDownloaderRedTube import DownloaderRedTube
from CDownloaderPornHub import DownloaderPornHub
from CDownloaderBeeg import DownloaderBeeg
from CDownloaderXHamster import DownloaderXHamster
from CDownloaderEporner import DownloaderEporner
# ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida

if len(sys.argv) == 6:
    server = str(sys.argv[1])
    search = str(sys.argv[2])
    first_page = int(sys.argv[3])
    last_page = int(sys.argv[4])
    output_dir = str(sys.argv[5])

    if server == 'XVideos':
        print("-----------------------------------------------------------")
        print("server: XVideos")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderXvideos(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'YouPorn':
        print("-----------------------------------------------------------")
        print("server: YouPorn")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderYouPorn(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'RedTube':
        print("-----------------------------------------------------------")
        print("server: RedTube")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderRedTube(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'PornHub':
        print("-----------------------------------------------------------")
        print("server: PornHub")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderPornHub(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'Beeg':
        print("-----------------------------------------------------------")
        print("server: Beeg")
        print("search: " + search)
        print("The page is unique for this server.")
        print("-----------------------------------------------------------")
        downloader = DownloaderBeeg(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'XHamster':
        print("-----------------------------------------------------------")
        print("server: XHamster")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderXHamster(output_dir, search, first_page, last_page)
        downloader.download()
    elif server == 'EPorner':
        print("-----------------------------------------------------------")
        print("server: EPorner")
        print("search: " + search)
        print("page " + str(first_page) + " to " + str(last_page))
        print("-----------------------------------------------------------")
        downloader = DownloaderEporner(output_dir, search, first_page, last_page)
        downloader.download()
    else:
        print('Server not found')
else:
    print('ERROR: Waiting arguments...')
