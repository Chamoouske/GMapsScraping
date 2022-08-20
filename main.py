from factory.browser.factory import FactoryBrowser
from factory.window.window import Janela


if __name__ == '__main__':
    janela = Janela()
    janela.config_root(title='Busca no Maps')
    janela.create_labels()
    janela.create_buttons()
    janela.loop()
