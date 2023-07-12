import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(1872,86,duration=2)
    sleep(1)
    pyautogui.click(94,135,duration=2)
    sleep(1)
    pyautogui.click(1342,146,duration=2)
    sleep(1)
    pyautogui.click(1242,117,duration=2)
    sleep(1)
    pyautogui.click(951,644,duration=2)

while True:
    # 1 - Navegar até o site https://www.instagram.com
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1)
    # VPS ou máquina virtual

    # 2 - Entrar com meu usário
    pyautogui.click(1145,360,duration=2)
    pyautogui.typewrite('SEUEMAIL.com')
    sleep(1)
    # 3 - Entrar com a minha senha
    pyautogui.click(1142,402,duration=2)
    pyautogui.typewrite('SUASENHA')
    sleep(1)
    # 4 - Clicar em 'Log In'
    pyautogui.click(1167,458,duration=2)
    sleep(10)
    # 5 - Clicar em 'Not Now' para não salvar navegador
    # pyautogui.click(x,y,duration=1)
    # sleep(10)
    # 6 - fechar janela de 'salvar senha'
    # pyautogui.click(x,y,duration=1)
    # sleep(2)
    # 7 - pesquisar pela página 
    pyautogui.click(96,250,duration=2)
    sleep(2)
    pyautogui.click(259,182,duration=1.5)
    sleep(2)
    pyautogui.typewrite('labflydrones')
    sleep(2)
    # 8 - Entrar na página 
    pyautogui.move(0, 60,duration=1.5)
    pyautogui.click()
    sleep(2)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(780,594, duration=1.5)
    sleep(2)
    # 10 - Verificar se já curti ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 6 horas
    if coracao is not None:
        logout()
        sleep(21600)
    # 12 - Se não tiver curtido, curtir a foto e comentar
    elif coracao == None:
        pyautogui.click(1101,890, duration=1.5)
        sleep(5)
        pyautogui.click(1224,991,duration=1.5)
        sleep(2)
        pyautogui.typewrite('Achei o trabalho de captura das imagens excepcional, continuem assim!')
        sleep(2)
        pyautogui.click(1539,989,duration=1.5)
        sleep(2)
        logout()
        sleep(21600)
# 15 - Após a 24 horas rodar tudo de novo