import pyautogui
import pyautogui as pag

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Word', 'Google', 'Notepad'])

if opcao == "Word":
    print("Escolheu Word")
elif opcao == "Google":
    print("Escolheu Google")
elif opcao == "Notepad":
    print("Escolheu Notepad")

