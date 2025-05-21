# Este programa é um menu interativo para o EchoDownload, um downloader de vídeos e áudios.
# Ele permite que o usuário escolha entre baixar um vídeo único, um áudio ou uma playlist.
# O programa é desenvolvido em Python e utiliza a biblioteca InquirerPy para criar um menu interativo.
# O menu é exibido em um formato amigável e colorido, com opções claras para o usuário.
# O programa também exibe informações sobre o desenvolvedor e o repositório do projeto no GitHub.
# O EchoDownload é um projeto open-source, e o código-fonte está disponível no GitHub.


# -*- coding: utf-8 -*-
from InquirerPy import inquirer
import EchoDownload


# Título do programa
print("\033[94m╔═══════════════════════════════════════════════╗")
print("║           Bem-vindo ao EchoDownload!          ║")
print("║              Download de Vídeos               ║")
print("║                                               ║")
print("║              Versão 1.0 - 2025                ║")
print("║               Desenvolvido em                 ║")
print("║  https://github.com/HOkket/EchoDownload.git   ║")
print("╚═══════════════════════════════════════════════╝\033[0m")


def menu():
    resposta = inquirer.select(
        message="Escolha o tipo de download que deseja fazer:",
        choices=["Vídeo Unico", "Áudio", "Playlist de Videos",
                 "Playlist de audios", "Sair"]
    ).execute()
    if resposta == "Vídeo Unico":
        EchoDownload.download_video()
    elif resposta == "Áudio":
        EchoDownload.download_audio()
    elif resposta == "Playlist":
        EchoDownload.download_playlist()
    elif resposta == "Playlist de audios":
        EchoDownload.download_playlist_audio()
    elif resposta == "Sair":
        print("Saindo do programa...")
        # Fim do programa
        print("\033[94m╔═══════════════════════════════════════════════╗")
        print("║       Obrigado por usar o EchoDownload!       ║")
        print("╚═══════════════════════════════════════════════╝\033[0m")
        print("\033[0m")
        print("Se esse programa te ajudou, considere avaliar o projeto em:")
        print("       https://github.com/HOkket/EchoDownload.git ")
        exit()


menu()
