from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

import time
import pandas as pd

from src.utils.vars import *


class Browser:
    """
    Class Browser with methods to search for restaurants in Google Maps using Selenium
    """
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
        """
        Method to navigate in the url of the site
        :param url_site: url of the site
        :return: None
        """
        self.driver.get(url_site)
        pass


    def close(self):
        """
        Method to close the browser
        :return: None
        """
        self.driver.quit()
        pass


    def generate_excel(self):
        """
        Method to generate a excel file with the results of the search
        :return: None
        """
        df = pd.DataFrame(self.restaurants)
        df.drop_duplicates(inplace=True)
        df.to_excel('./resultados.xlsx', index=False)


    def search_locals(self, search_string=''):
        """
        Method to search for restaurants in Google Maps
        :param search_string: string to search for restaurants
        :return: None
        """
        self.get('https://www.google.com/maps')
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, xpath_search_input).send_keys(search_string, Keys.ENTER)
        self.update_elements_results()


    def update_elements_results(self):
        """
        Method to show all results of the search
        :return: None
        """
        continue_search = True
        while continue_search:
            self.scroll_div_to_show_all_results(xpath_div_results)
            continue_search = self.get_elements_in_results()

        self.generate_excel()
        self.close()


    def get_elements_in_results(self):
        """
        Method to get the elements in the results of the search
        :return: boolean
        """
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
        """
        Method to scroll and show all results of the search
        :return: None
        """
        self.wait_until_element_is_not_displayed(xpath_div_results)
        self.scroll_div_to_show_all_results(xpath_div_results)


    def wait_until_element_is_not_displayed(self, element):
        """
        Method to wait until the element is not displayed
        :param element: element to wait
        :return: None
        """
        WebDriverWait(self.driver, timeout=60)\
            .until(lambda driver: driver.find_element(By.XPATH, element)\
            .is_displayed())


    def scroll_div_to_show_all_results(self, div):
        """
        Method to scroll the div to show all results of the search
        :param div: div to scroll
        :return: None
        """
        try:
            WebDriverWait(self.driver, timeout=5).until(lambda driver: driver.find_element(By.XPATH, div).send_keys(Keys.PAGE_DOWN))
        except TimeoutException:
            pass


    def get_values_in_element(self, element):
        """
        Method to get the values in the element
        :param element: element to get the values
        :return: None
        """
        try: element.click()
        except: pass
        time.sleep(3)
        self.wait_until_element_is_not_displayed(xpath_result_details)
        restaurant_name = self.get_restaurant_name()
        restaurant_address = self.get_restaurant_address()
        restaurant_phone = self.get_restaurant_phone()
        
        self.save_value_results(restaurant_name, restaurant_address, restaurant_phone)

    
    def get_restaurant_name(self):
        """
        Method to get the name of the restaurant
        :return: string
        """
        try: return self.driver.find_element(By.XPATH, xpath_result_details_name).text
        except: return 'Sem nome informado!'

    
    def get_restaurant_address(self):
        """
        Method to get the address of the restaurant
        :return: string
        """
        try: return self.driver.find_element(By.XPATH, xpath_result_details_address).text
        except: 
            try: return self.driver.find_element(By.XPATH, xpath_result_details_address2).text
            except: return 'Sem endereço informado!'
    

    def get_restaurant_phone(self):
        """
        Method to get the phone of the restaurant
        :return: string
        """
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

        return restaurant_phone


    def save_value_results(self, name, address, phone):
        """
        Method to save the values in the dict results
        :param name: name of the restaurant
        :param address: address of the restaurant
        :param phone: phone of the restaurant
        :return: None
        """
        self.restaurants['nome'].append(name)
        self.restaurants['endereco'].append(address)
        self.restaurants['telefone'].append(phone)
