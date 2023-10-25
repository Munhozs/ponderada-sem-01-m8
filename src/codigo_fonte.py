from machine import Pin
from utime import sleep

led = Pin(5, Pin.OUT) #atribui o LED na porta 5
btn = Pin(26, Pin.IN) #atribui o botão na porta 26
is_led_on = False #rastreia o estado do LED

while True:
    #verifica se o botão foi clicado e o LED aceso
    if btn.value() == 1:
        if not is_led_on:
            print("botão clicado! Ligando LED...")
            led.value(1) #liga o LED ao clicar no botão
            is_led_on = True
            sleep(2) #faz o LED apagar depois de 2 segundos
            led.value(0) #apaga o LED
            is_led_on = False
    

  