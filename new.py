import pyfirmata
import message as wa # Importing The Code for Sending message
comport='COM4'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:7:o')# Setting up the pins
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')
buzzer=board.get_pin('d:8:o')



def led(total):
    if total==0:
        #danger
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        buzzer.write(1)
        
        



    elif total==1:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        buzzer.write(0)
        
       

    elif total==2:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        buzzer.write(0)
        # wa.work(total)# Sending message VIA Twilio
      

    elif total==3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
        buzzer.write(0)
       

    elif total==4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
        buzzer.write(0)
        # wa.work(total)
       

    elif total==5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        buzzer.write(0)
       

