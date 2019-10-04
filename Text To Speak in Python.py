# Desenvolvedor Brevetecno
# Converter Texto em voz
# Python 3
# 2019

import pyttsx3 as tts

# Inicia o sintetizador de voz
voz = tts.init()

while True:
    print('='*50)

    # O texto que deve ser convertido em síntese de voz
    cmd = str(input('Falar: '))

    try:
        voz.say(cmd)
        voz.runAndWait()
    except:
        print('Ocorreu algum erro durante o processo.')
    
    print('='*50)
