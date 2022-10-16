import tkinter as tk
from tkinter import messagebox

from src.browser.factory import FactoryBrowser


class Window:
    """
    Class to create a window to search for local on Google Maps
    """
    def __init__(self):
        self.root = tk.Tk()

        self.buttons = []
        self.labels = []

        self.my_grid = [3, 2]
        self.last_grid_usage = [0, 0]

        self.driver = False
        self.local_input = False
        self.num_pages = False
        self.num_browsers = 2

    def config_root(self,title='Busca no Maps', geometry='300x100'):
        """
        Method to configure the root window
        :return: None
        """
        self.root.title(title)

    def loop(self):
        """
        Method to start the window loop
        :return: None
        """
        self.root.mainloop()
        self.driver.close()

    def create_buttons(self):
        """
        Method to create the buttons of the window
        :return: None
        """
        self.buttons.append(tk.Button(self.root,text='Pesquisar no Chrome', command=lambda: self.search_locals('chrome')))
        row, column = self.define_grid_for_element()
        self.buttons[-1].grid(row=row, column=column, padx=10, pady=10)

        self.buttons.append(tk.Button(self.root,text='Pesquisar no Edge', command=lambda: self.search_locals('edge')))
        row, column = self.define_grid_for_element()
        self.buttons[-1].grid(row=row, column=column, padx=10, pady=10)

    def define_grid_for_element(self):
        """
        Method to define the grid position for the next element
        :return: row, column
        """
        if self.last_grid_usage[1] < self.my_grid[1]:
            self.last_grid_usage[1] += 1
        else:
            self.last_grid_usage[0] += 1
            self.last_grid_usage[1] = 1

        row = self.last_grid_usage[0]
        column = self.last_grid_usage[1]

        return row, column

    def create_labels(self):
        """
        Method to create the labels of the window
        :return: None
        """
        self.labels.append(tk.Label(self.root,text='O que deseja pesquisar?'))
        row, column = self.define_grid_for_element()
        self.labels[-1].grid(row=row, column=column, padx=10, pady=10)
        self.create_input()

    def create_input(self):
        """
        Method to create the input of the window
        :return: None
        """
        if not self.local_input:
            self.local_input = tk.Entry()
            row, column = self.define_grid_for_element()
            self.local_input.grid(row=row, column=column, padx=10, pady=10)
        elif not self.num_pages:
            self.num_pages = tk.Entry()
            row, column = self.define_grid_for_element()
            self.num_pages.grid(row=row, column=column, padx=10, pady=10)

    def search_locals(self,browser='chrome'):
        """
        Method to show window to search for local on Google Maps
        :param browser: str
        :return: None
        """
        messagebox.showinfo("Aviso", "Clique em ok para iniciar a busca!\nOutro aviso será exibido ao final do processo!")
        self.create_webdriver(browser)
        self.driver.search_locals(self.local_input.get())
        messagebox.showinfo("Aviso",f"A pesquisa foi finalizada!\nProcure a planilha na mesma pasta deste executável!")

    def create_webdriver(self, browser='chrome'):
        """
        Method to instantiate the Browser class
        :param browser: str
        :return: None
        """
        self.driver = FactoryBrowser(browser)
