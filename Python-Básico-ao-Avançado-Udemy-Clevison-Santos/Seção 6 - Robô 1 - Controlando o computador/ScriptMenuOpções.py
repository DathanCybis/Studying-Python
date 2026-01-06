import pyautogui
import pyautogui as pag

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Word', 'Google', 'Notepad'])

if opcao == "Word":
    print("Escolheu Word")

    pag.hotkey('win', 'r')

    pag.sleep(0.5)

    pag.typewrite('winword')

    pag.sleep(0.5)

    pag.press('enter')

    pag.sleep(1)

    pag.click(x=268, y=219)

    pag.sleep(0.5)

    pag.typewrite("Escolheu abrir o word")

    #print(pag.position())


elif opcao == "Google":
    print("Escolheu Google")

    pag.hotkey('win', 'r')

    pag.sleep(0.5)

    pag.typewrite('chrome')

    pag.sleep(0.5)

    pag.press('enter')

    pag.sleep(0.5)

    pag.typewrite('Escolheu abrir o google')


elif opcao == "Notepad":
    print("Escolheu Notepad")

    pag.hotkey('win', 'r')

    pag.sleep(0.5)

    pag.typewrite('notepad')

    pag.sleep(0.5)

    pag.press('enter')

    pag.sleep(0.5)

    pag.typewrite("Escolheu abrir o notepad")

