class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ["telewizor niezaprogramowany, brak dostępnych kanałów"]
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
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
                print("Telewizor jest załączony")
                print(f"Numer kanału: {self.channel_no}. {self.channels[self.channel_no-1]}")
            except IndexError:
                print(f"Numer kanału: {self.channel_no}. (kanały niezaprogramowane)")
        else:
            print("Telewizor jest wyłączony")
            
TV = TV()
TV.show_status()
TV.on()
TV.show_status()
TV.show_channels()
TV.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox"])
TV.show_channels()
TV.set_channel(5)
TV.show_status()
TV.off()
TV.show_status()


