import pyautogui

'''Aqui o primeiro passo é salvar no computador uma imagem simples e dar
um nome a ela. Podemos fazer isso com o capture. Feito isso,
vamos dar sequencia nos comandos abaixo.'''

print(pyautogui.locateOnScreen('numero4.png'))
    
# Resposta: Box(left=1377, top=714, width=31, height=33)   
 

# Agora vamos encontrar o PONTO CENTRAL DE UMA IMAGEM

print(pyautogui.locateCenterOnScreen('numero4.png'))
# Resposta: Point(x=1355, y=435)

# Com essas informações, podemos, por exemplo, dar um click

pyautogui.click(x=1355, y=435, duration=2)
 
 