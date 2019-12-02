class TV():
    def __init__(self):
        self.is_on = False
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print("Telewizor jest załączony")
        else:
            print("Telewizor jest wyłączony")
            
TV = TV()
TV.show_status()
TV.on()
TV.show_status()
TV.off()
TV.show_status()

            
