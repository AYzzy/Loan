class Bike:
    def __init__(self):
        self.__is_on = False
        self.__gear = 0
        self.__speed = 0


    def power(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True
        self.__speed = 0


    def turn_off(self):
        self.__is_on = False

    def current_gear(self):
        return self.__gear

    def accelerate(self):
        if self.__is_on == True:
            if self.__speed < 20:
                self.__speed += 1
                self.__gear = 1
            elif self.__speed >= 20 and self.__speed < 30:
                self.__speed += 2
                self.__gear = 2
            elif self.__speed >= 30 and self.__speed < 41:
                self.__speed +=3
                self.__gear = 3
            else:
                self.__speed += 4
                self.__gear = 4


    def current_speed(self):
        return self.__speed

    def decelerate(self):
        if self.__is_on == True:
            if self.__speed < 1:
                self.__speed -= 0
                self.__gear = 0
            elif self.__speed >= 1 and self.__speed <= 20:
                self.__speed -= 1
                self.__gear = 1
            elif self.__speed > 20 and self.__speed <= 30:
                self.__speed -= 2
                self.__gear = 2
                if self.__speed == 20:
                    self.__gear = 1
            elif self.__speed > 30 and self.__speed <= 40:
                self.__speed -= 3
                self.__gear = 3
                if self.__speed == 30:
                    self.__gear = 2
            else:
                self.__speed -= 4
                if self.__speed <= 40:
                    self.__gear = 3
