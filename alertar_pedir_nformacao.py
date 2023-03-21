
import pyautogui


# Para criar um alerta que a automação vai começar através ..
# ...de uma tela de aviso
pyautogui.alert(text='Iniciando automação', title='Automação de login',
                button='ok')



# Pedindo informações ao usuario:
email = pyautogui.prompt(text='Digite seu email', title='Informações obrigatorias')

print(f'Você digitou {email}')


