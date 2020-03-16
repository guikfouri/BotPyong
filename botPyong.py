import time
import os
import json
from selenium import webdriver

''' 
    Script criado para votar automaticamente no Pyong
'''

class PyongForaBot():

    def __init__(self):
        self.url = 'https://login.globo.com/login/4728?tam=widget&url=https%3A%2F%2Fintervencao.globo.com%2Fintervencoes%2Fshow.do%3Fpopin%3Dtrue%26servicoId%3D4728%26urlIntervencao%3Dhttps%3A%2F%2Fs.glbimg.com%2Fgl%2Fba%2Fbarra-globocom.callback.html%2523https%253A%252F%252Fgshow.globo.com%252Frealities%252Fbbb%252Fbbb20%252Fvotacao%252Fparedao-bbb20-quem-voce-quer-eliminar-babu-pyong-ou-rafa-6bb86a70-ac24-48e7-bdb8-a6cd83009ef3.ghtml'

    def findBrowserVersion(self):
        # self.browser_version = (self.driver.capabilities['browserVersion'])
        self.browser_version = '80'
        path = os.getcwd()  
        path += '/Drivers/' + str(self.browser_version[0:2]) + '.exe'
        print(path)
        return path

    def openDriver(self, path):
        self.driver = webdriver.Chrome(executable_path=path)  # Inicia o browser
        self.driver.get(self.url)  # Acessar a URL especificada

    def login(self):
        with open('login.json') as f:
            data = json.load(f)
            login = data['login']
            passw = data['senha']

        email_in = self.driver.find_element_by_xpath('//*[@id="login"]')
        email_in.send_keys(login)

        passw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        passw_in.send_keys(passw)

        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[6]/button').click()

    def vote(self):
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div').click()
                time.sleep(1)

                self.driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/img').click()
                time.sleep(3)

                self.driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[3]/div/div/div[1]/div[2]/button').click()
            except:
                pass

bot = PyongForaBot()
path = bot.findBrowserVersion()
bot.openDriver(path)
bot.login()
bot.vote()