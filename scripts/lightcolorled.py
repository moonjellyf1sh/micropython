from machine import Pin, PWM
import utime

color1= PWM(Pin(14))
color1.freq(500) #Hz

color2 = PWM(Pin(15))
color2.freq(600) #Hz

color3 = PWM(Pin(28))
color3.freq(600)
color3.duty_u16(100*500)

color4 = PWM(Pin(22))
color4.freq(800)
color4.duty_u16(110*1000)

for i in range(100):
    color1.duty_u16(i*655)
    color2.duty_u16((100-i)*655)
    utime.sleep_ms(100)