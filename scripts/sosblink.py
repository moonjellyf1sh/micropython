#emely 1/20
#blinks

from include.rcc_library import Raft
import utime

myraft = Raft()

myraft.led_on()
utime.sleep_ms(200)
myraft.led_off()

myraft.led_on()
utime.sleep_ms(100)
myraft.led_off()


