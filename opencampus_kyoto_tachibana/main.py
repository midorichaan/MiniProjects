import hat
import i2c_bus, unit
import ustruct
import machine

from m5stack import *
from m5ui import *
from uiflow import *
from micropython import const
from m5stack import timEx

#init
setScreenColor(color)

#attrs
_E6_AD_A3_E9_9D_A2_E3_82_BB_E3_83_B3_E3_82_B5 = None
_E5_8F_B3_E5_81_B4_E3_82_BB_E3_83_B3_E3_82_B5 = None
_E6_AD_A3_E9_9D_A2_E8_B7_9D_E9_9B_A2 = None
_E5_8F_B3_E5_81_B4_E8_B7_9D_E9_9B_A2 = None
hat_roverc0 = hat.get(hat.ROVERC)
labelF = M5TextBox(2, 5, "F", lcd.FONT_Default, 0xFFFFFF, rotate=0)
labelR = M5TextBox(2, 30, "R", lcd.FONT_Default, 0xFFFFFF, rotate=0)
front = M5TextBox(17, 5, "0000", lcd.FONT_Default, 0xFFFFFF, rotate=0)
right = M5TextBox(17, 30, "0000", lcd.FONT_Default, 0xFFFFFF, rotate=0)
mm0 = M5TextBox(55, 5, "mm", lcd.FONT_Default, 0xFFFFFF, rotate=0)
mm1 = M5TextBox(55, 30, "mm", lcd.FONT_Default, 0xFFFFFF, rotate=0)
_MODEL_ID = const(0xc0)
_REVISION_ID = const(0xc2)
_START = const(0x00)
_RANGE_STATUS = const(0x14)
_SCL_SDA__EXTSUP_HV = const(0x89)
_MSRC_CONFIG_CONTROL = const(0x60)
_ADDR = const(0x29)

while not (btnA.isPressed()):
    hat_roverc0.SetSpeed(0, 0, 0)

class MyTof:
    def __init__(self, port):
        self.i2c = i2c_bus.get(port)
        self._available()
        self.state = 0
        self.distance = 0

    def _register_char(self, register, value=None, buf=bytearray(1)):
        if value is None:
            self.i2c.readfrom_mem_into(_ADDR, register, buf)
            return buf[0]

        ustruct.pack_into("<b", buf, 0, value)
        return self.i2c.writeto_mem(_ADDR, register, buf)

    def _register_short(self, register, value=None, buf=bytearray(2)):
        if value is None:
            self.i2c.readfrom_mem_into(_ADDR, register, buf)
            return ustruct.unpack(">h", buf)[0]

        ustruct.pack_into(">h", buf, 0, value)
        return self.i2c.writeto_mem(_ADDR, register, buf)

    def _available(self):
        if self.i2c.is_ready(_ADDR) or self.i2c.is_ready(_ADDR):
            pass
        else:
            raise unit.Unit("TOF unit maybe not connect")

    def _update(self):
        try:
            if self.state == 0:
                self._register_char(_START, 0x01)
                self.state = 1
            elif self.state == 1:
                data = self._register_char(0x14)
                if data & 0x01:
                    self.state = 0
                    distance = self._register_short(0x14 + 10)
                    if distance != 20:
                        self.distance = distance
        except:
            pass

    def value(self):
        self._update()
        self._update()
        return self.distance
      
_E6_AD_A3_E9_9D_A2_E3_82_BB_E3_83_B3_E3_82_B5 = MyTof(unit.PAHUB0)
_E5_8F_B3_E5_81_B4_E3_82_BB_E3_83_B3_E3_82_B5 = MyTof(unit.PAHUB1)

while True:
    _E6_AD_A3_E9_9D_A2_E8_B7_9D_E9_9B_A2 = _E6_AD_A3_E9_9D_A2_E3_82_BB_E3_83_B3_E3_82_B5.value()
    _E5_8F_B3_E5_81_B4_E8_B7_9D_E9_9B_A2 = _E5_8F_B3_E5_81_B4_E3_82_BB_E3_83_B3_E3_82_B5.value()
    front.setText(str(_E6_AD_A3_E9_9D_A2_E8_B7_9D_E9_9B_A2))
    right.setText(str(_E5_8F_B3_E5_81_B4_E8_B7_9D_E9_9B_A2))
    if _E5_8F_B3_E5_81_B4_E8_B7_9D_E9_9B_A2 >= 150:
      hat_roverc0.SetSpeed(0, 30, (-30))
    elif _E6_AD_A3_E9_9D_A2_E8_B7_9D_E9_9B_A2 < 100:
      hat_roverc0.SetSpeed(0, 0, 30)
    else:
      hat_roverc0.SetSpeed((-10), 30, 0)

    wait_ms(2)
      hat_roverc0.SetSpeed(0, 0, 30)
