from src.window.window import Window


if __name__ == '__main__':
    janela = Window()
    janela.config_root(title='Busca no Maps')
    janela.create_labels()
    janela.create_buttons()
    janela.loop()
