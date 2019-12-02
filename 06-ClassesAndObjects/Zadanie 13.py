class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channels(self,channels_list):
        self.channels = channels_list 
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def show_status(self):
        if self.is_on == True:
            print(f"Telewizor jest załączony, Numer kanału: {self.channel_no} {self.channels[self.channel_no]}")
        except IndexError:
            print(f"t")
        else:
            print("Telewizor jest wyłączony")
            
TV = TV()
TV.show_status()
TV.on()
TV.show_status()
TV.set_channels(["TVN","POLSAT"])
TV.show_status()
TV.off()
TV.show_status()


