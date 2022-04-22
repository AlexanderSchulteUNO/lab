class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        self.channel = 0
        self.volume = 0
        self.on = False
        pass

    def power(self) -> None:
        '''
        Toggles the Television's On Status
        '''
        if self.on == False:
            self.on = True
        else:
            self.on = False
        pass

    def channel_up(self) -> None:
        '''
        Cycles the Television's Channel Status up by 1
        '''
        if self.on == True:
            if self.channel == 3:
                self.channel = 0
            else:
                self.channel += 1
        pass

    def channel_down(self) -> None:
        '''
        Cycles the Television's Channel Status down by 1
        '''
        if self.on == True:
            if self.channel == 0:
                self.channel = 3
            else:
                self.channel -= 1
        pass

    def volume_up(self) -> None:
        '''
        Cycles the Television's Volume Status up by 1
        '''
        if self.on == True:
            if self.volume < 2:
                self.volume += 1
        pass

    def volume_down(self) -. None:
        '''
        Cycles the Television's Volume Status down by 1
        '''
        if self.on == True:
            if self.volume > 0:
                self.volume -= 1
        pass

    def __str__(self) -> str:
        '''
        Gives a report on the Television's Status
        '''
        return("TV status: Is on = {}, Channel = {}, Volume = {}".format(self.on, self.channel, self.volume))
        pass
