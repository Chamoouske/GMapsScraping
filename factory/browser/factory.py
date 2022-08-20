from selenium import webdriver

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from .browser import Browser


def FactoryBrowser(browser='chrome'):
    browsers = {
        'chrome': Chrome,
        'firefox': Firefox,
        'edge': Edge
    }

    return browsers[browser]()


class Chrome(Browser):
    def __init__(self, occult=False):
        self.options = webdriver.ChromeOptions()
        self.def_occult(occult)
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, chrome_options=self.options)

    def def_occult(self, occult):
        if occult:
            self.options.add_argument("--headless")


class Firefox(Browser):
    def __init__(self, occult=False):
        self.options = webdriver.FirefoxProfile()
        self.def_occult(occult)
        service = FirefoxService(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, firefox_profile=self.options)

    def def_occult(self, occult):
        if occult:
            self.options.add_argument("--headless")


class Edge(Browser):
    def __init__(self, occult=False):
        self.options = webdriver.EdgeOptions()
        self.def_occult(occult)
        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service, options=self.options)

    def def_occult(self, occult):
        if occult:
            self.options.add_argument("--headless")
