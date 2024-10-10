class AirConditioner:
    def __init__(self):
        self.__temperature = 0
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        self.__temperature = 16


    def turn_off(self):
        self.__is_on = False

    def power(self):
        return self.__is_on

    def current_temperature(self):
        return self.__temperature

    def increase(self):
        if self.__is_on == True:
            if self.__temperature < 30:
                self.__temperature += 1
            else:
                self.__temperature = 30

    def decrease(self):
        if self.__is_on == True:
            if self.__temperature > 16:
                self.__temperature -= 1
            else:
                self.__temperature = 16