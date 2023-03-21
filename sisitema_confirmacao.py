import pyautogui

# Para confirmar, por exemplo, se a automação vai continuar ou não

resposta = pyautogui.confirm(text='continuar rodando nossa automação?',
                             title='Confirmação', buttons=['sim','não', 'cancelar'])

if resposta == 'sim':
    print('Continuando automação')
elif resposta == 'não':
    print('Parar automação')
else:
    print('Fechando programa')
            