class SmartDevice:
    def __init__(self, brand, model, power_consumption, is_on=False):
        self._brand=brand
        self._model=model
        self._power_consumption=power_consumption
        self._is_on=is_on
    def toggle_power(self):
        self._is_on=not self._is_on
        
    def get_info(self):
        return f"{self._brand} {self._model}"


class SmartLight(SmartDevice):
    def __init__(self, brand, model, power_consumption, is_on=False, brightness=0):
        super().__init__(brand, model, power_consumption, is_on)
        self._brightness=brightness
    def set_brightness(self, level):
        if level>=0 and level<=100 and self._is_on:
            self._brightness=level
            print("Successfully changed")
        else:
            print("invalid brightness level or Light On first")
    def get_info(self):
        return f"{self._brand} {self._model}"


class SmartThermostat(SmartDevice):
    def __init__(self, brand, model, power_consumption, is_on=False, temperature=20 ):
        super().__init__(brand, model, power_consumption, is_on)
        self._temperature= temperature
    def set_temperature(self, temp):
        self._temperature= temp
        
    def toggle_power(self):
        self._is_on= not self._is_on
        if not self._is_on:
            print("Saving energy settings...")
    def get_info(self):
        return f"{self._brand} {self._model}"
            


smartdevice= SmartLight("TVS", "AK50", 30, True, 40)
print(smartdevice.get_info())
print(smartdevice.toggle_power())
print(smartdevice.set_brightness(600))
print(smartdevice.toggle_power())
print(smartdevice.set_brightness(60))

smartdevice1=SmartThermostat("FZ", "IU900", 30, False, 90)

print(smartdevice1.get_info())
print(smartdevice1.toggle_power())
print(smartdevice1.set_temperature(60))
print(smartdevice1.toggle_power())
print(smartdevice1.set_temperature(60))


            
    
    
        
    
    
