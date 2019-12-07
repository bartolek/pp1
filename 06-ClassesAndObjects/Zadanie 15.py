class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ["telewizor niezaprogramowany, brak dostępnych kanałów"]
        self.volume = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def increase_volume(self):
        if self.volume==10:
            print("==Nie można bardziej podłośnić TV==")
        else:
            self.volume+=1
    def decrease_volume(self):
        if self.volume==0:
            print("==Nie można bardziej wyciszyć TV==")
        else:
            self.volume-=1
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, new_channels):
        self.channels = new_channels
        print("Programowanie kanałów...")
    def show_channels(self):
        if (len(self.channels))>1:
            print("LISTA KANAŁÓW TV:")
            for i in range(len(self.channels)):
                print(f"{i+1}: {self.channels[i]}")
        else:
            print("LISTA KANAŁÓW TV: \n ------------")
            
        
    def show_status(self):
        if self.is_on == True:
            try:
                print(f"Telewizor jest załączony, Numer kanału: {self.channel_no}. {self.channels[self.channel_no-1]}      Głośność: {self.volume}")
            except IndexError:
                print(f"Numer kanału: {self.channel_no}. (kanały niezaprogramowane)")
        else:
            print("Telewizor jest wyłączony")
            
TV = TV()
TV.show_status()
TV.on()
TV.show_status()
TV.show_channels()
TV.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox","TVP3", "HBO"])
TV.show_channels()
TV.increase_volume()
TV.set_channel(5)
TV.show_status()
TV.increase_volume()
TV.increase_volume()
TV.set_channel(3)
TV.show_status()
TV.set_channel(7)
TV.decrease_volume()
TV.show_status()
TV.off()
TV.show_status()