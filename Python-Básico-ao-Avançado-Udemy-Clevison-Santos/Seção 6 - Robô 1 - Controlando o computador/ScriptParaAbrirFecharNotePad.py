import pyautogui as pag

pag.hotkey('win', 'r')

pag.sleep(1)

pag.typewrite('notepad')

pag.sleep(1)

pag.press('enter')

pag.sleep(1)

pag.typewrite('O notepad foi aberto')

pag.sleep(1)

fecharJanela = pag.getActiveWindow()

fecharJanela.close()
