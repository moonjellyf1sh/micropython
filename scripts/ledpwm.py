from machine import Pin, PWM 

pin = 13 #number for gpio pin

pwm_pin = PWM(Pin(pin))
#frequency is cycle per second (Hertz, Hz)
pwm_pin.freq(300) #Hz

percent = 30

pwm_pin.duty_u16(percent*655)