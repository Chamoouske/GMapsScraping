from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

import time
import pandas as pd

from utils.vars import *


class Browser:
    restaurants = {
        'nome': [],
        'endereco': [],
        'telefone': []
    }

    total_results = 0
    last_results = 0

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Browser, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get(self, url_site):
        self.driver.get(url_site)
        pass

    def close(self):
        self.driver.quit()
        pass

    def generate_excel(self):
        df = pd.DataFrame(self.restaurants)
        df.drop_duplicates(inplace=True)
        df.to_excel('./resultados.xlsx', index=False)

    def search_locals(self, search_string='', num_pages=False):
        self.get('https://www.google.com/maps')
        self.num_pages = num_pages
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, xpath_search_input).send_keys(search_string, Keys.ENTER)
        self.update_elements_results()

    def update_elements_results(self):
        continue_search = True
        while continue_search:
            self.scroll_div_to_show_all_results(xpath_div_results)
            continue_search = self.get_elements_in_results()

        self.generate_excel()
        self.close()

    def get_elements_in_results(self):
        self.show_all_results()
        elements = self.driver.find_elements(By.XPATH, xpath_result)
        self.total_results = len(elements)
        if self.last_results == self.total_results:
            return False
        for element in elements[self.last_results:]:
            try:
                if element.is_displayed():
                    self.get_values_in_element(element)
            except StaleElementReferenceException:
                pass
        self.last_results = self.total_results
        return True

    def show_all_results(self):
        self.wait_until_element_is_not_displayed(xpath_div_results)
        self.scroll_div_to_show_all_results(xpath_div_results)

    def wait_until_element_is_not_displayed(self, element):
        WebDriverWait(self.driver, timeout=60)\
            .until(lambda driver: driver.find_element(By.XPATH, element)\
            .is_displayed())

    def scroll_div_to_show_all_results(self, div):
        try:
            WebDriverWait(self.driver, timeout=5).until(lambda driver: driver.find_element(By.XPATH, div).send_keys(Keys.PAGE_DOWN))
        except TimeoutException:
            pass

    def get_values_in_element(self, element):
        try: element.click()
        except: pass
        time.sleep(3)
        try:
            self.wait_until_element_is_not_displayed(xpath_result_details)
            restaurant_name = self.driver.find_element(By.XPATH, xpath_result_details_name).text
            restaurant_address = self.driver.find_element(By.XPATH, xpath_result_details_address).text
        except:
            try:
                restaurant_address = self.driver.find_element(By.XPATH, xpath_result_details_address2).text
            except:
                restaurant_address = 'Sem endereço informado!'
        restaurant_phone = None
        web_elements_in_results = self.driver.find_elements(By.XPATH, xpath_result_details_phone)
        for web_element in web_elements_in_results:
            try:
                if 'Telefone' in web_element.get_attribute('aria-label'):
                    restaurant_phone = web_element.get_attribute('aria-label').replace('Telefone: ', '')
            except:
                pass
        if restaurant_phone == None:
            web_elements_in_results = self.driver.find_elements(By.XPATH, xpath_result_details_phone2)
            for web_element in web_elements_in_results:
                try:
                    if 'Telefone' in web_element.get_attribute('aria-label'):
                        restaurant_phone = web_element.get_attribute('aria-label').replace('Telefone: ', '')
                except:
                    pass
        if restaurant_phone == None:
            restaurant_phone = 'Sem telefone disponível!'
        self.save_value_results(restaurant_name, restaurant_address, restaurant_phone)

    def save_value_results(self, name, address, phone):
        self.restaurants['nome'].append(name)
        self.restaurants['endereco'].append(address)
        self.restaurants['telefone'].append(phone)
