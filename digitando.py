import pyautogui, pyperclip

# mover mouse até o campo para digitar

# clicar no campo digitar

# digitar a mensagem

# clicar em enviar

pyautogui.move(1500,85, duration=2)

pyautogui.click()

# o typewrite funciona bem, porém, ele não tem assentos, ç e tal.
pyautogui.typewrite('Ola, bom dia')

pyautogui.click(15500, 85)



# pyperclip serve para gerar os caracteres como assentos, ç, etc
# Então, podemos fazer uma função para colocar assentos e outros na frase
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v') #este comando aciona as teclas
    
# Daí agora usar a função criada

escrever_frase('olá, bom dia!')
    
