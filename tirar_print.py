import pyautogui

#pyautogui.screenshot('aqui.jpg')  # Vai tirar print da tela toda


# Aqui vamos pegar uma parte da dela delimitando as coordenadas corretas.
# Veja, os dois primeiros números represetam a coordenada que pegaremos..
# ..utilizando o programa mouseInfo. Depois vamos adicionar manualmente ..
# .. as coordenadas pra direita e para baixo.
pyautogui.screenshot('somenteUmaPArte.jpg', region=(129,495, 400, 500))


# RESUMO ACIMA, primeiros dois numeros: Coordenadas principais
# Restante, quantos pixels pra direita, quantos px pra esquerda


