import pyautogui

pyautogui.moveTo(1826,46, duration=2)  # aqui pegaremos a coordenada com o mouseInfo e adicionaremos a coordenada.

# duration é o tempo que ele vai levar pra ir de ponto a ponto

# para rodar o programa, abra o terminal e digite python + nome do arquivo. Ex: python movimentar_clicar.py


# aqui movimentamos o mouse após o comando moveTo(), sendo X para esquerda(valores negativos) e direita(valores positivos) e y cima(negativo) e baixo(positivo)
pyautogui.move(-50, 0, duration=2) 

pyautogui.click() # ao não passar nenhum parametro, ele vai clicar onde o mouse passou


# Aqui são as configurações da função click. interval é o tempo entre um click e outro (em segundos)
pyautogui.click(x=300, y=250, clicks=2, interval=1, button='left', duration=2)
# Não sou obrigado a usar todos esses parametros. Exemplos abaixo:
pyautogui.click(button='right')
pyautogui.click(clicks=10)
# E existem funções prontas:
pyautogui.doubleClick() # clica duas vezes
pyautogui.middleClick() # botão do meio
pyautogui.rightClick() # botão da direita






