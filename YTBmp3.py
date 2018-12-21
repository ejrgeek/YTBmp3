"""
Feito por Erlon Dantas da Nóbrega Júnior
GitHub > github.com/ejrgeek
Nome: YTBmp3
Descrição: A aplicação baixa o video do YouTube e converte para MP3
Uso: Só é preciso executar via terminal e digitar a URL do video e dar enter, o video vai ser baixado na raiz do arquivo

requeriments: yotube_dl
* pip instal youtube_dl *
GitHub: https://github.com/rg3/youtube-dl
"""

import youtube_dl as ytb
class YTBmp3:

    def __init__(self):
        self.ydl = ytb.YoutubeDL(self.mp3Options())

    def status(self, d):
        if d['status'] == 'finished':
            print('\033[33m' + '\033[1m' + "DOWNLOAD CONCLUIDO, CONVERTENDO..."+'\033[0;0m')

    def mp3Options(self):
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [self.status],
        }

    def baixar(self, url):
        print('\033[34m' + '\033[1m' + "INICIANDO DOWNLOAD" + '\033[0;0m')
        self.ydl.download([url])


if __name__ == "__main__":

    print('\033[31m' + """__   __ _____ ______                    _____ 
\ \ / /|_   _|| ___ \                  |____ |
 \ V /   | |  | |_/ / _ __ ___   _ __      / /
  \ /    | |  | ___ \| '_ ` _ \ | '_ \     \ \\
  | |    | |  | |_/ /| | | | | || |_) |.___/ /
  \_/    \_/  \____/ |_| |_| |_|| .__/ \____/ 
                                | |           
                                |_|
Coder: Erlon \"ejrgeek\" Junior
GitHub: github.com/ejrgeek""" + '\033[0;0m')

    while True:
        try:
            objDownload = YTBmp3()
            url = input('\033[36m' + '\033[1m'+"URL > " + '\033[0;0m')
            objDownload.baixar(url)
            print('\033[32m' + '\033[1m' + "CONCLUIDO" + '\033[0;0m')
            break
        except ytb.utils.DownloadError as ERROR:
            print('\033[31m' + '\033[1m' + "Insira uma URL válida" + '\033[0;0m')
        except ValueError as e:
            print("Erro inesperado")
