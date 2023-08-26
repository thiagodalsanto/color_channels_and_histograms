## Color Channels and Histograms
Projeto com uma aplicação simples de interface gráfica (GUI) desenvolvida utilizando a biblioteca Tkinter do Python para conversão e análise de imagens. A aplicação permite aos usuários abrir um arquivo de imagem e realizar várias conversões de espaço de cores, utilizando OpenCV. Além disso, a aplicação oferece funcionalidades para analisar e salvar imagens de canais individuais e seus histogramas. 

## Sobre o trabalho:

* Disciplina: OP63I-CC8 - Processamento De Imagens E Reconhecimento De Padrões	
* Turma: 2023/2 - 8º Período
* Docente: Pedro Luiz de Paula Filho

## Recursos 
- **Abrir Imagem:** Clique no botão "Abrir Imagem" para carregar um arquivo de imagem (formatos suportados: PNG, JPG, JPEG, BMP, GIF).
- **Conversão:** Escolha entre várias opções de conversão, incluindo RGB para vários espaços de cores (HSI, HSV, HSL, CMYK, XYZ, YCrCb) e escala de cinza.
- **Análise de Canais e  Imagem Convertida:** A imagem convertida é exibida em uma janela separada, da mesma forma que todos os canais individuais de cores.
- **Salvar Canais e Imagem Convertida:** Salve os canais de cores individuais e imagem convertida como arquivos de imagem separados.
- **Salvar Histogramas:** Salve os histogramas dos canais de cores como arquivos de imagem.
- **Exibir Histogramas:** Exiba histogramas dos canais de cores com rótulos e títulos.

## Dependências

Siga essa ordem de instalação para garantir que não exista conflito de versões:
1. Python 3 `pip install python3`
2. NumPy `pip install numpy`
3. OpenCV (cv2) `pip install opencv-python`
4. Matplotlib `pip install matplotlib`
5. Tkinter (Geralmente já vem instalado com o Python no Windows, para o Linux utilizar o comando `sudo apt-get install python3-tk`)

## Como Utilizar

1. Clone o repositório do GitHub: `git clone https://github.com/thiagodalsanto/color_channels_and_histograms.git`
2. Instale as dependências utilizadas
3. Execute o aplicativo em uma IDE.

## Imagens do Programa

Disposição da Imagem Convertida (RGB Original), e os três canais individuais (Red, Green e Blue).
![Imagem1](https://i.imgur.com/GM5dVgM.png)

Imagem completa do programa com Imagem convertida de RGB para HSI (Hue, Saturation e Intensity), com os três canais individuais, a interface GUI simples ao lado e os Histogramas gerados.
![Imagem2](https://i.imgur.com/CC60FYs.png)  
