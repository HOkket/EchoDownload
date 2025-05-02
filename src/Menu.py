
# -*- coding: utf-8 -*-
from InquirerPy import inquirer
import EchoDownload
import yt_dlp as youtube_dl
import os


# Título do programa
print("\033[94m╔═══════════════════════════════════════════════╗")
print("║           Bem-vindo ao EchoDownload!          ║")
print("║              Download de Vídeos               ║")
print("║                                               ║")
print("║              Versão 1.0 - 2025                ║")
print("║               Desenvolvido em                 ║")
print("║  https://github.com/HOkket/EchoDownload.git   ║")
print("╚═══════════════════════════════════════════════╝\033[0m")

if __name__ == "__main__":
    resposta = inquirer.select(
        message="Escolha o tipo de download que deseja fazer:",
        choices=["Vídeo Unico", "Áudio", "Playlist", "Sair"]
    ).execute()
    if resposta == "Vídeo Unico":
        EchoDownload.download_video()
    elif resposta == "Áudio":
        EchoDownload.download_audio()
    elif resposta == "Playlist":
        EchoDownload.download_playlist()
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
