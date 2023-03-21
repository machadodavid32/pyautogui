import pyautogui

#Como pedir uma senha na tela e mostrar a digitação de forma criptografada

senha = pyautogui.password(text='Digite sua senha', title='Dados de login',
                           mask='*')

print(senha)
