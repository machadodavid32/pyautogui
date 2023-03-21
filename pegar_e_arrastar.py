# pegar e arrastar algo para outro lugar

import pyautogui



# Abrir a ferramenta para descobrir as coordenadas.
# >>> from mouseinfo import mouseInfo
# >>> mouseInfo()

#Aqui ele vai e clica para arrastar
pyautogui.moveTo(269,638, duration=2)

#Aqui ele leva para o local de destino
pyautogui.dragTo(369,814, button='left', duration=2)

