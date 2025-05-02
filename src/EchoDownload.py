
# EchoDownload - Download de vídeos do YouTube
import yt_dlp as youtube_dl
import os
import sys


def download_video():
    rodar = "SIM"
    # inicio do loop
    while rodar == "SIM" or rodar == "S" or rodar == "sim" or rodar == "s":
        # URL do vídeo a ser baixado
        url = input("Digite o URL do vídeo do YouTube: ")
        print("\033[93mAguarde enquanto o programa verifica o URL...\033[0m")
#  Verifica se o URL é válido
        while not url.startswith("https://youtu.be") and not url.startswith("https://youtube.com"):
            print(
                "\033[91mURL inválido. Por favor, insira um URL do YouTube válido.\033[0m")
            url = input("Digite o URL do vídeo do YouTube: ")
# Define o diretório de saída com base no sistema operacional
        if sys.platform.startswith('win'):
            # Windows
            usuário = os.getenv('USERNAME', 'usuário_padrão')
            output_local = f"C:/Users/{usuário}/Downloads"
        elif sys.platform.startswith('linux'):
            # Linux
            usuário = os.getenv('USER', 'usuário_padrão')
            output_local = f"/home/{usuário}/Downloads"
        else:
            # Outros sistemas operacionais
            print("\033[91mSistema operacional não suportado.\033[0m")
            exit()
# Verifica se o diretório de saída existe, se não, cria
        if not os.path.exists(output_local):
            os.makedirs(output_local)
# Configurações para o yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': output_local + '/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
        }
        print("\033[91mIniciando o download...\033[0m")
        print(
            "\033[91mPor favor, aguarde enquanto o download está em andamento...\033[0m")
# Usa o yt-dlp para baixar o vídeo e áudio no melhor formato disponível.
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                # Exibe a animação de carregamento
                ydl.download([url])
                print(
                    f"\033[92mDownload concluído com sucesso! O arquivo foi salvo em: {output_local}\033[0m")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
# Pergunta ao usuário se deseja continuar
        rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
        if rodar == "NAO" or rodar == "N" or rodar == "nao" or rodar == "n":
            print("\033[91mSaindo do programa...\033[0m")
            # Fim do programa
            print("\033[94m╔═══════════════════════════════════════════════╗")
            print("║           Obrigado por usar o EchoDownload!           ║")
            print("╚═══════════════════════════════════════════════╝\033[0m")
            print("\033[0m")
            print("Se esse programa te ajudou, considere avaliar o projeto em:")
            print("        https://github.com/HOkket/EchoDownload.git ")
            exit()
        elif rodar != "SIM" and rodar != "S" and rodar != "sim" and rodar != "s":
            while rodar != "SIM" and rodar != "NAO" and rodar != "S" and rodar != "N" and rodar != "sim" and rodar != "s" and rodar != "nao" and rodar != "n":
                print(
                    "\033[91mOpção inválida. Por favor, insira 'SIM' ou 'NAO'.\033[0m")
                rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
            # Fim do loop
# Fim do loop


def download_audio():
    rodar = "SIM"
    # inicio do loop
    while rodar == "SIM" or rodar == "S" or rodar == "sim" or rodar == "s":
        # URL do vídeo a ser baixado
        url = input("Digite o URL do vídeo do YouTube: ")
        print("\033[93mAguarde enquanto o programa verifica o URL...\033[0m")
#  Verifica se o URL é válido
        while not url.startswith("https://youtu.be") and not url.startswith("https://youtube.com"):
            print(
                "\033[91mURL inválido. Por favor, insira um URL do YouTube válido.\033[0m")
            url = input("Digite o URL do vídeo do YouTube: ")
# Define o diretório de saída com base no sistema operacional
        if sys.platform.startswith('win'):
            # Windows
            usuário = os.getenv('USERNAME', 'usuário_padrão')
            output_local = f"C:/Users/{usuário}/Downloads"
        elif sys.platform.startswith('linux'):
            # Linux
            usuário = os.getenv('USER', 'usuário_padrão')
            output_local = f"/home/{usuário}/Downloads"
        else:
            # Outros sistemas operacionais
            print("\033[91mSistema operacional não suportado.\033[0m")
            exit()
# Verifica se o diretório de saída existe, se não, cria
        if not os.path.exists(output_local):
            os.makedirs(output_local)
# Configurações para o yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': output_local + '/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
        }
        print("\033[91mIniciando o download...\033[0m")
        print(
            "\033[91mPor favor, aguarde enquanto o download está em andamento...\033[0m")
# Usa o yt-dlp para baixar o vídeo e áudio no melhor formato disponível.
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                # Exibe a animação de carregamento
                ydl.download([url])
                print(
                    f"\033[92mDownload concluído com sucesso! O arquivo foi salvo em: {output_local}\033[0m")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        # Pergunta ao usuário se deseja continuar
        rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
        if rodar == "NAO" or rodar == "N" or rodar == "nao" or rodar == "n":
            print("\033[91mSaindo do programa...\033[0m")
            # Fim do programa
            print("\033[94m╔═══════════════════════════════════════════════╗")
            print("║           Obrigado por usar o EchoDownload!           ║")
            print("╚═══════════════════════════════════════════════╝\033[0m")
            print("\033[0m")
            print("Se esse programa te ajudou, considere avaliar o projeto em:")
            print("        https://github.com/HOkket/EchoDownload.git ")
            exit()
        elif rodar != "SIM" and rodar != "S" and rodar != "sim" and rodar != "s":
            while rodar != "SIM" and rodar != "NAO" and rodar != "S" and rodar != "N" and rodar != "sim" and rodar != "s" and rodar != "nao" and rodar != "n":
                print(
                    "\033[91mOpção inválida. Por favor, insira 'SIM' ou 'NAO'.\033[0m")
                rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
            # Fim do loop
# Fim do loop


def download_playlist():
    rodar = "SIM"
    # inicio do loop
    while rodar == "SIM" or rodar == "S" or rodar == "sim" or rodar == "s":
        # URL da playlist a ser baixada
        url = input("Digite o URL da playlist do YouTube: ")
        print("\033[93mAguarde enquanto o programa verifica o URL...\033[0m")
#  Verifica se o URL é válido
        while not url.startswith("https://youtu.be") and not url.startswith("https://youtube.com"):
            print(
                "\033[91mURL inválido. Por favor, insira um URL do YouTube válido.\033[0m")
            url = input("Digite o URL da playlist do YouTube: ")
# Define o diretório de saída com base no sistema operacional
        if sys.platform.startswith('win'):
            # Windows
            usuário = os.getenv('USERNAME', 'usuário_padrão')
            output_local = f"C:/Users/{usuário}/Downloads"
        elif sys.platform.startswith('linux'):
            # Linux
            usuário = os.getenv('USER', 'usuário_padrão')
            output_local = f"/home/{usuário}/Downloads"
        else:
            # Outros sistemas operacionais
            print("\033[91mSistema operacional não suportado.\033[0m")
            exit()
# Verifica se o diretório de saída existe, se não, cria
        if not os.path.exists(output_local):
            os.makedirs(output_local)
# Configurações para o yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': output_local + '/%(playlist)s/%(title)s.%(ext)s',
            'noplaylist': False,
            'quiet': True,
        }
        print("\033[91mIniciando o download...\033[0m")
        print(
            "\033[91mPor favor, aguarde enquanto o download está em andamento...\033[0m")
# Usa o yt-dlp para baixar o vídeo e áudio no melhor formato disponível.
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                # Exibe a animação de carregamento
                ydl.download([url])
                print(
                    f"\033[92mDownload concluído com sucesso! O arquivo foi salvo em: {output_local}\033[0m")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        # Pergunta ao usuário se deseja continuar
        rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
        if rodar == "NAO" or rodar == "N" or rodar == "nao" or rodar == "n":
            print("\033[91mSaindo do programa...\033[0m")
            # Fim do programa
            print("\033[94m╔═══════════════════════════════════════════════╗")
            print("║           Obrigado por usar o EchoDownload!           ║")
            print("╚═══════════════════════════════════════════════╝\033[0m")
            print("\033[0m")
            print("Se esse programa te ajudou, considere avaliar o projeto em:")
            print("        https://github.com/HOkket/EchoDownload.git ")
            exit()
        elif rodar != "SIM" and rodar != "S" and rodar != "sim" and rodar != "s":
            while rodar != "SIM" and rodar != "NAO" and rodar != "S" and rodar != "N" and rodar != "sim" and rodar != "s" and rodar != "nao" and rodar != "n":
                print(
                    "\033[91mOpção inválida. Por favor, insira 'SIM' ou 'NAO'.\033[0m")
                rodar = input("Deseja continuar? (SIM/NAO): ").strip().upper()
            # Fim do loop
# Fim do loop
