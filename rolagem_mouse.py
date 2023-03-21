import pyautogui

from time import sleep

# rolagem do mouse
# Em uma tela onde existe barra de rolagem, apos chegar la com moveTo(),..


pyautogui.scroll(-1500)  # vai descer 1500 pixels

pyautogui.scroll(500) # vai subir 500 pixels

# Podemos colocar isso num laço de repetição:
for i in range(20):
    pyautogui.scroll(-500, duration=2)
    sleep(2)

# Acima ele vai descer a pagina -500 pixels 20 vezes


