import yt_dlp as youtube_dl
import os
import time
from tqdm import tqdm  # Biblioteca para animação de carregamento

# Título do programa
print("\033[94m╔════════════════════════════════════════╗")
print("║        Bem-vindo ao EchoDownload!      ║")
print("╚════════════════════════════════════════╝\033[0m")

url = input("Digite o URL do vídeo do YouTube: ")  # URL do vídeo a ser baixado
# Voltar para 'usuário_padrão' se USER não estiver definido
usuário = os.getenv('USER', 'usuário_padrão')
output_local = f"/home/{usuário}/Downloads"  # Local onde o vídeo será salvo

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
print("\033[91mPor favor, aguarde enquanto o download está em andamento...\033[0m")

# Animação de carregamento


def loading_animation():
    for _ in tqdm(range(100), desc="\033[92mBaixando\033[0m", ascii=True):
        time.sleep(0.05)


# Usa o yt-dlp para baixar o vídeo e áudio no melhor formato disponível.
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    try:
        loading_animation()  # Exibe a animação de carregamento
        ydl.download([url])
        print(
            f"Download completed successfully. O arquivo foi salvo em: {output_local}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
