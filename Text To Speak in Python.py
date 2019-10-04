# Desenvolvedor Brevetecno
# Converter Texto em voz
# Python 3
# 2019

# Biblioteca
import pyttsx3 as tts

# Inicia o sintetizador de voz
voz = tts.init()

# Loop
while True:
    print('='*50)

    # O texto que deve ser convertido em síntese de voz
    cmd = str(input('Falar: '))

    try:
        # Adiciona o que deve ser dito
        voz.say(cmd)
        
        # Reproduzir o comando transformado em voz
        voz.runAndWait()
    except:
        # Caso aconteça algum erro
        print('Ocorreu algum erro durante o processo.')
    
    print('='*50)
