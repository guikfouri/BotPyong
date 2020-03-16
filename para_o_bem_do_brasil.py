from selenium import webdriver
import time
import os
import json

''' 
    Script criado para votar automaticamente no Pyong
'''

class PyongForaBot():

    def __init__(self):
        self.url = 'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-babu-pyong-ou-rafa-6bb86a70-ac24-48e7-bdb8-a6cd83009ef3.ghtml'

    def findBrowserVersion(self):
        #self.browser_version = self.driver.capabilities['browserVersion']
        self.browser_version = '80'
        path = os.getcwd()  
        path += '/Drivers/' + str(self.browser_version[0:2]) + '.exe'
        print(path)
        driver = webdriver.Chrome(executable_path=path) 

    def openDriver(self):
        self.driver = webdriver.Chrome()  # Inicia o browser
        self.driver.get(self.url)  # Acessar a URL especificada

    def login(self):
        with open('login.json') as f:
            data = json.load(f)
            login = data['login']
            passw = data['senha']

        self.signin = self.driver.find_elements_by_class_name('barra-botao-entrar')[0].click()
        email_in = self.driver.find_element_by_xpath()
        email_in.send_keys(login)

        passw_in = self.driver.find_element_by_xpath()
        passw_in.send_keys(passw)
    def votar(self):
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div').click()
                time.sleep(1)

                driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img').click()
                time.sleep(3)

                driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[3]/div/div/div[1]/div[2]/button').click()
            except:
                pass