#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import time
import RPi.GPIO as GPIO
import MFRC522
 
# UID dos cartões que possuem acesso liberado.
CARTOES_LIBERADOS = {
    'B0:3B:2:C5:4C': 'Gabriela'
}

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

try:
    # Inicia o módulo RC522.
    LeitorRFID = MFRC522.MFRC522()
 
    print('Aproxime seu cartão RFID')
 
    while True:
        # Verifica se existe uma tag próxima do módulo.
        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)
 
        if status == LeitorRFID.MI_OK:
            print('Cartão detectado!')
 
            # Efetua leitura do UID do cartão.
            status, uid = LeitorRFID.MFRC522_Anticoll()
 
            if status == LeitorRFID.MI_OK:
                uid = ':'.join(['%X' % x for x in uid])
                print('UID do cartão: %s' % uid)
 
                # Se o cartão está liberado exibe mensagem de boas vindas.
                if uid in CARTOES_LIBERADOS:
                    print('Acesso Liberado!')
                    print('Olá %s.' % CARTOES_LIBERADOS[uid])
                    
                    GPIO.output(12, GPIO.HIGH)
                    GPIO.output(40, 0)
                    print('Abrindo porta...')

                    time.sleep(1)

                    GPIO.output(12, GPIO.LOW)
                    GPIO.output(40, 1)
                    print('Porta aberta...')
                else:
                    print('Acesso Negado!')
                    
                    GPIO.output(16, GPIO.HIGH)
                    time.sleep(2)
                    GPIO.output(16, GPIO.LOW)

                print('\nAproxime seu cartão RFID')
 
        time.sleep(.25)
except KeyboardInterrupt:
    # Se o usuário precionar Ctrl + C
    # encerra o programa.
    GPIO.cleanup()
    print('\nPrograma encerrado.')
