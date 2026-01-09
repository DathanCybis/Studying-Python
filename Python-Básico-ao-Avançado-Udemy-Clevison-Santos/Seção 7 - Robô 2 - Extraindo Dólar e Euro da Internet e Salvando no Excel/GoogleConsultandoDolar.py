from selenium import webdriver as opcoes
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from selenium.webdriver.common.by import By

navegador = opcoes.Chrome()

navegador.get("https://www.google.com/")

pag.sleep(1)

navegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

pag.sleep(1)

navegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

pag.sleep(1)

valorDolar = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

pag.sleep(1)

print(valorDolar)
