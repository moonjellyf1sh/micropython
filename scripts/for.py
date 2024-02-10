from include.rcc_library import Raft 
import utime
myraft = Raft()

for i in range(5):
    myraft.led_on()
    utime.sleep_ms(1000)
    myraft.led_off()
    utime.sleep_ms(1000)

for i in range(8):
    myraft.led_on()
    utime.sleep_ms(500)
    myraft.led_off()
    utime.sleep_ms(500)