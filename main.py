import cv2
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk 
from tkinter import filedialog

class ImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("200x650") 
        self.image = None
        self.conversion_code = None
        self.conversion_name = None 
        self.channel_windows = []
        self.hist_windows = []

        self.title_label = Label(root, text="Baguncinha com Imagens", font=("Helvetica", 14), wraplength=180)
        self.title_label.pack()

        # Estilo para botões
        button_style = ttk.Style()
        button_style.configure("TButton",
                               padding=5,  # Espaçamento interno
                               relief="raised",  # Efeito de relevo
                               background="#3498db",  # Cor de fundo
                               font=("Helvetica", 12),
                               foreground="white")  # Cor do texto

        self.menu_frame = Frame(root)
        self.menu_frame.pack()

        self.load_button = ttk.Button(self.menu_frame, text="Abrir Imagem", command=self.load_image, style="TButton")
        self.load_button.pack(fill=X)  # Deixar da largura da janela (horizontal)

        conversions = [
            ("RGB (Original)", None),
            ("RGB to HSI", cv2.COLOR_BGR2HLS_FULL),
            ("RGB to HSV", cv2.COLOR_BGR2HSV),
            ("RGB to HSL", cv2.COLOR_BGR2HLS),
            ("RGB to CMYK", cv2.COLOR_BGR2YCR_CB),
            ("RGB to XYZ", cv2.COLOR_BGR2XYZ),
            ("RGB to YCrCb", cv2.COLOR_BGR2YCR_CB),
            ("Tons de Cinza", cv2.COLOR_BGR2GRAY),
        ]

        for name, code in conversions:
            button = ttk.Button(self.menu_frame, text=name, command=lambda n=name, c=code: self.perform_conversion(n, c), style="TButton")
            button.pack(fill=X)

        self.save_channel_button = ttk.Button(self.menu_frame, text="Salvar Canais", command=self.save_channels, style="TButton")
        self.save_converted_image_button = ttk.Button(self.menu_frame, text="Salvar Imagem Convertida", command=self.save_converted_image, style="TButton")
        self.save_histograms_button = ttk.Button(self.menu_frame, text="Salvar Histogramas", command=self.save_histograms, style="TButton")
        self.show_histograms_button = ttk.Button(self.menu_frame, text="Abrir Histogramas", command=self.show_histograms, style="TButton")

        self.save_channel_button.pack(fill=X)
        self.save_converted_image_button.pack(fill=X)
        self.save_histograms_button.pack(fill=X)
        self.show_histograms_button.pack(fill=X)

        self.footer_label = Label(root, text="Desenvolvido por Thiago", font=("Helvetica", 10))
        self.footer_label.pack(side=BOTTOM, pady=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(initialdir="./", title="Selecionar Imagem", filetypes=(("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"), ("Todos os arquivos", "*.*")))
        if file_path:
            self.image = cv2.imread(file_path)

    def perform_conversion(self, conversion_name, conversion_code):
        self.conversion_code = conversion_code
        self.conversion_name = conversion_name

        if conversion_code is None:
            self.converted_image = self.image
        else:
            self.converted_image = cv2.cvtColor(self.image, conversion_code)

        cv2.imshow("Imagem Convertida", self.converted_image)
        self.channel_windows = ["Imagem Convertida"]
        self.hist_windows = []

        channels = cv2.split(self.converted_image)

        channel_names = ["Canal Blue", "Canal Green", "Canal Red"]

        for i, channel in enumerate(channels):
            if len(channel.shape) == 2:
                channel_image = cv2.cvtColor(channel, cv2.COLOR_GRAY2BGR)
            else:
                channel_image = channel
            cv2.imshow(channel_names[i], channel_image)
            self.channel_windows.append(channel_names[i])

            hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
            self.hist_windows.append(hist)

        cv2.waitKey(1)
        self.root.wait_window()

    def save_channels(self):
        if self.conversion_code is not None:
            for i, channel_name in enumerate(self.channel_windows[1:]):
                cv2.imwrite(f"canal_{i}.png", cv2.split(self.converted_image)[i])
                print(f"Canal {i} salvo com sucesso!")

    def save_converted_image(self):
        if self.conversion_code is not None:
            cv2.imwrite("imagem_convertida.png", self.converted_image)
            print("Imagem Convertida salva com sucesso!")

    def save_histograms(self):
        if self.conversion_code is not None:
            for i, (hist, channel_name) in enumerate(zip(self.hist_windows, self.channel_windows[1:])):
                plt.figure()
                plt.plot(hist)
                plt.xlim([0, 256])
                plt.savefig(f"histogram_{channel_name}.png")
                plt.close()
                print(f"Histograma do Canal {channel_name} salvo com sucesso!")

    def show_histograms(self):
        if self.conversion_code is not None:
            hist_names = self.channel_windows[1:]
            plt.figure(num=f"Histogramas - {self.conversion_name}", figsize=(12, 5))

            for i, (hist, hist_name) in enumerate(zip(self.hist_windows, hist_names)):
                plt.subplot(1, 3, i+1)
                plt.plot(hist)
                plt.xlim([0, 256])
                plt.ylim(0, max(hist))
                plt.title(hist_name)
                plt.xlabel("Níveis de Intensidade")
                plt.ylabel("Frequência")

            plt.tight_layout(rect=[0, 0.05, 1, 0.95])
            plt.suptitle(self.conversion_name)
            plt.show()

if __name__ == "__main__":
    root = Tk()
    app = ImageConverter(root)
    root.mainloop()
