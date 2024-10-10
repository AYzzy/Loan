
class Television:

    def __init__(self):
        self.volume = int
        self.__is_on = False
        self.channel = int
        self.mute_initial_value = int

    def power(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True
        self.channel = 1
        self.volume = 2

    def turn_off(self):
        self.__is_on = False

    def get_channel(self):
        if self.__is_on == True:
            return self.channel
        else:
            raise ValueError('The television is not on')

    def set_channel(self, channel_number):
        if channel_number > 100 or channel_number < 1:
            raise ValueError('The channel number must be less than 100')
        self.channel = channel_number


    def get_volume(self):
        return self.volume

    def set_volume(self, volume_number):
        if self.__is_on == True:
            if volume_number > 10 or volume_number < 1:
                raise ValueError('The volume number must be less than 1 or greater than 10')
            else:
                self.volume = volume_number
        else:
            raise ValueError('The Television is not on')

    def channel_up(self):
        if self.__is_on == True:
            if self.channel > 99:
                self.channel = self.channel
            else:
                self.channel += 1

    def channel_down(self):
        if self.__is_on == True:
            if self.channel < 1:
                raise ValueError('The channel number must be greater than or equal to 1')
            else:
                self.channel -= 1
        else:
            raise ValueError('The Television is not on')

    def volume_up(self):
        if self.__is_on == True:
            if self.volume > 10:
                self.volume = self.volume
            else:
                self.volume += 1
        else:
            raise ValueError('The Television is not on')

    def volume_down(self):
        if self.__is_on == True:
            if self.volume < 1:
                self.volume = self.volume
            self.volume -= 1
        else:
            raise ValueError('The Television is not on')

    def mute(self):
        if self.__is_on == True:
            self.mute_initial_value = self.volume
            self.volume = 0
        else:
            raise ValueError('The Television is not on')

    def unmute(self):
        if self.__is_on == True:
            self.volume = self.mute_initial_value
        else:
            raise ValueError('The Television is not on')






