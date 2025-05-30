# EchoDownload

EchoDownload é um programa simples em python3 compativel com windows/linux que permite baixar vídeos do YouTube utilizando a biblioteca yt-dlp. O programa solicita ao usuário a URL do vídeo desejado, configura as opções de download e exibe uma animação de carregamento enquanto o vídeo é baixado.


## Instalação

### Voce pode baixar os binarios de Windows e Linux

<div style="display: flex; justify-content: space-around; align-items: center;">
   <a href="https://github.com/HOkket/EchoDownload/releases/download/Youtube/EchoDownload.exe">
      <img src="https://github.com/HOkket/EchoDownload/blob/main/img/WinDow.png" alt="Windows install" style="width: 45%; max-width: 200px;">
   </a>
   <a href="https://github.com/HOkket/EchoDownload/releases/download/Youtube/EchoDownload">
      <img src="https://github.com/HOkket/EchoDownload/blob/main/img/LinDow.png" alt="Linux install" style="width: 44%; max-width: 200px;">
   </a>
</div>

---

Voce tambem pode baixar os binarios de Windows e Linux [AQUI!](https://github.com/HOkket/EchoDownload/releases)
Para utilizar o EchoDownload direto do codigo fonte, você precisa ter o Python instalado em sua máquina. Além disso, é necessário instalar a biblioteca yt-dlp e InquirerPy. Você pode fazer isso utilizando o seguinte comando:

```
pip install yt-dlp InquirerPy
```

## Uso via terminal

1. Clone o repositório:
   ```
   git clone https://github.com/HOkket/EchoDownload.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd EchoDownload
   ```
3. Execute o programa:
   ```
   python src/main.py
   ```
4. Insira a URL do vídeo do YouTube que deseja baixar quando solicitado.
## Falta implementar

 * Opções de diferentes tipos de saída para vídeos e áudios
 * Uma GUI

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob os termos da [LICENSE](LICENSE).
