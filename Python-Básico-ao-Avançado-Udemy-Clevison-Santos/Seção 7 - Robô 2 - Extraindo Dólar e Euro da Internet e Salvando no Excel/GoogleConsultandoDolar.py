from selenium import webdriver as opcoes
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from selenium.webdriver.common.by import By

navegador = opcoes.Chrome()

navegador.get("https://www.google.com/")

pag.sleep(1)

navegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

pag.sleep(1)

